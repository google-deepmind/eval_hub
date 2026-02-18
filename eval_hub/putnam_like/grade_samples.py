# Copyright 2026 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

r"""Putnam-Like Grading Script.

This script iterates through a validated problem set, finds model-generated
samples that match a specific pattern, and uses the Gemini API to grade them
based on the problem's official grading scheme.

The output is a JSON file for each sample, structured like a human-graded
review.

Example usage (public):
export GEMINI_API_KEY=<YOUR_API_KEY>
python grade_samples.py --input_dir=./putnam_like --model_regex=gemini-2.5-pro --debug_k=2
# BEGIN GOOGLE-INTERNAL
export GEMINI_API_KEY=<YOUR_API_KEY>
blaze run //third_party/eval_hub/putnam_like:grade_samples -- \
  --input_dir=./putnam_like \
  --model_regex=gemini-2.5-pro \
  --debug_k=2 --alsologtostderr
# END GOOGLE-INTERNAL

Expected Input Directory Structure (--input-dir):
└── putnam_like_validated/
    └── {set_name}/
        └── {problem_name}/
            ├── metadata.json
            ├── question/
            │   └── question.md
            ├── rubrics/
            │   └── grading_scheme.md
            └── samples/
                └── {model_name_timestamp}/
                    ├── sample.md or sample_*.md
                    └── grade_{model_name}_{timestamp}_{sample_name}.json
"""

import collections
import concurrent.futures
import csv
import json
import os
import pathlib
import random
import re
import time

from absl import app
from absl import flags
from absl import logging
import google.ai.generativelanguage as glm
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as api_core_exceptions

FLAGS = flags.FLAGS
flags.DEFINE_string(
    "model_name",
    "gemini-2.5-pro",
    "The name of the Gemini model to use for grading.",
)
flags.DEFINE_string(
    "input_dir",
    "putnam_like_validated",
    "Input directory for the validated problem folders.",
)
flags.DEFINE_string(
    "model_regex",
    None,
    "Optional regex to filter model directories to grade (e.g.,"
    " 'gemini-2-5-pro_.*'). Applied to the parent directory of the sample"
    " file.",
)
flags.DEFINE_string(
    "sample_regex",
    None,
    "Optional regex to filter sample file names (e.g., 'sample_001_.*')."
    " Applied to the sample file name itself.",
)
flags.DEFINE_integer(
    "max_workers", 50, "Maximum number of parallel API requests."
)
flags.DEFINE_integer(
    "max_api_retries", 3, "Maximum number of retries for API calls."
)
flags.DEFINE_float("temperature", 0.0, "Temperature for model sampling.")
flags.DEFINE_integer(
    "debug_k", 0, "Run in debug mode with K random samples. If 0, runs on all."
)
flags.DEFINE_string(
    "to_csv", None, "If specified, write results to this CSV file."
)


SYSTEM_PROMPT_TEMPLATE = """
You are a meticulous and fair grader for a university-level mathematics competition.
Your task is to evaluate a student's solution based on a provided problem statement and a detailed grading scheme/rubric.

**INSTRUCTIONS:**
1.  First, carefully read the problem statement to understand the question.
2.  Next, study the grading rubric to understand exactly how points are awarded for each step.
3.  Then, analyze the provided student's solution step-by-step.
4.  Compare the student's work against the rubric to determine a final score. The score must be an integer between 0 and 10.
5.  Provide a concise comment explaining the reasoning for your grade.
6.  If there are errors in the solution, briefly categorize the types of mistakes made. If the solution is flawless, this can be null.

**OUTPUT FORMAT:**
Your final output MUST be a single, valid JSON object and nothing else. Do not wrap it in markdown fences. The JSON object must have the following structure:
{{
    "reviewer_id": "{model_name}",
    "grade": <integer between 0 and 10>,
    "comment": "<Your concise explanation for the grade>",
    "types_of_mistakes": "<A brief description of errors, or null if correct>"
}}
"""


def get_api_key() -> str | None:
  """Retrieves the Gemini API key from environment variables."""
  try:
    return os.environ["GEMINI_API_KEY"]
  except KeyError:
    logging.error("❌ FATAL: GEMINI_API_KEY environment variable not found.")
    return None


def grade_gemini_sample(
    input_path: pathlib.Path,
    sample_path: pathlib.Path,
    grader_timestamp: str,
    api_key: str,
):
  """Grades a single solution sample and saves the resulting JSON.

  Args:
      input_path: The base directory for relative path logging.
      sample_path: Path to the sample file to grade.
      grader_timestamp: Timestamp string for the grading session.
      api_key: The Gemini API key.

  Returns:
      A tuple containing:
        - A status string ("SUCCESS", "SKIPPED", or "FAILURE").
        - The path to the saved grade file (or None if grading failed or
        skipped).
        - A dictionary containing data for the CSV row, or None.
  """
  # Robustly find the problem directory by locating the 'samples' directory
  problem_dir = sample_path
  while problem_dir.name != "samples":
    problem_dir = problem_dir.parent
  problem_dir = problem_dir.parent  # The actual problem dir is parent of 'samples'

  output_filename = (
      f"grade_{FLAGS.model_name}_{grader_timestamp}_{sample_path.stem}.json"
  )
  output_path = sample_path.parent / output_filename

  if output_path.exists():
    return "SKIPPED", None, None

  logging.info(
      "  -> Grading: %s", sample_path.relative_to(input_path)
  )

  try:
    # Load all necessary content
    question = (problem_dir / "question" / "question.md").read_text(
        encoding="utf-8"
    )
    grading_scheme = (problem_dir / "rubrics" / "grading_scheme.md").read_text(
        encoding="utf-8"
    )
    solution_to_grade = sample_path.read_text(encoding="utf-8")

    # Construct the full prompt
    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(model_name=FLAGS.model_name)
    parts = [
        glm.Part(text=system_prompt),
        glm.Part(text="\n--- PROBLEM STATEMENT ---\n"),
        glm.Part(text=question),
        glm.Part(text="\n--- GRADING RUBRIC ---\n"),
        glm.Part(text=grading_scheme),
        glm.Part(text="\n--- STUDENT'S SOLUTION TO GRADE ---\n"),
        glm.Part(text=solution_to_grade),
    ]

    client_options = client_options_lib.ClientOptions(api_key=api_key)
    client = glm.GenerativeServiceClient(client_options=client_options)
    generation_config = glm.GenerationConfig(
        temperature=FLAGS.temperature, response_mime_type="application/json"
    )
    request = glm.GenerateContentRequest(
        model=f"models/{FLAGS.model_name}",
        contents=[glm.Content(parts=parts)],
        generation_config=generation_config,
    )

    # Call API with retry logic
    for attempt in range(FLAGS.max_api_retries):
      try:
        response = client.generate_content(request)
        raw_response_text = response.candidates[0].content.parts[0].text

        # Robustly find the JSON block in the response
        json_match = re.search(r"\{.*\}", raw_response_text, re.DOTALL)
        if not json_match:
          raise ValueError("No JSON object found in the response.")
        parsed_json = json.loads(json_match.group(0))

        # Validate the parsed JSON structure
        required_keys = ["reviewer_id", "grade", "comment", "types_of_mistakes"]
        if not all(key in parsed_json for key in required_keys):
          raise ValueError(
              "JSON response is missing one or more required keys:"
              f" {required_keys}"
          )

        grade = parsed_json["grade"]
        if not isinstance(grade, int) or not (0 <= grade <= 10):
          raise ValueError(
              f"Grade '{grade}' is not an integer between 0 and 10."
          )

        # If validation passes, write to file and return
        with open(output_path, "w", encoding="utf-8") as f:
          json.dump(parsed_json, f, indent=4)
        csv_data = {
            "question": question,
            "sample": solution_to_grade,
            "grade": parsed_json["grade"],
        }
        return "SUCCESS", output_path, csv_data

      except (
          api_core_exceptions.GoogleAPICallError,
          ValueError,
          json.JSONDecodeError,
      ) as e:
        logging.warning(
            "     - WARNING: Grading failed on attempt %d: %s", attempt + 1, e
        )

        time.sleep(2**attempt)  # Exponential backoff

    logging.error(
        "     - ❌ FAILURE: Could not get a valid grade for %s after all"
        " retries.",
        sample_path.name,
    )
    return "FAILURE", None, None

  except FileNotFoundError as e:
    logging.error("  -> ❌ ERROR reading files for %s: %s", sample_path.name, e)
    return "FAILURE", None, None
  except Exception as e:  # pylint: disable=broad-exception-caught
    logging.error(
        "  -> ❌ An unexpected error occurred for %s (%s): %s",
        sample_path.name,
        type(e).__name__,
        e,
    )
    return "FAILURE", None, None


def main(argv):
  """Main function to run the sample grading pipeline."""
  del argv  # Unused.
  api_key = get_api_key()
  if not api_key:
    exit(1)

  input_dir = FLAGS.input_dir
  workspace_dir = os.environ.get("BUILD_WORKSPACE_DIRECTORY")
  if workspace_dir:
    input_path = pathlib.Path(workspace_dir) / input_dir
  else:
    input_path = pathlib.Path(input_dir)

  if not input_path.is_dir():
    logging.error("❌ Error: Input directory '%s' not found.", input_path)
    return

  glob_pattern = "**/sample*.md"
  all_samples = sorted(input_path.rglob(glob_pattern))

  # Find all sample files, optionally filtering by regex
  filtered_samples = []
  for p in all_samples:
    model_dir_match = True
    if FLAGS.model_regex:
      if not re.search(FLAGS.model_regex, str(p.parent.name)):
        model_dir_match = False

    sample_file_match = True
    if FLAGS.sample_regex:
      if not re.search(FLAGS.sample_regex, str(p.name)):
        sample_file_match = False

    if model_dir_match and sample_file_match:
      filtered_samples.append(p)

  all_samples = filtered_samples

  if FLAGS.model_regex:
    logging.info(
        "Filtering model directories by r'%s'", FLAGS.model_regex
    )
  if FLAGS.sample_regex:
    logging.info(
        "Filtering sample files by r'%s'", FLAGS.sample_regex
    )

  if not all_samples:
    logging.warning(
        "No sample files found matching the specified criteria in '%s'.",
        FLAGS.input_dir,
    )

  # Debug mode logic
  if FLAGS.debug_k > 0 and len(all_samples) > FLAGS.debug_k:
    logging.info(
        "\n🔬 DEBUG MODE: Selecting K=%d random samples...", FLAGS.debug_k
    )
    all_samples = random.sample(all_samples, FLAGS.debug_k)

  # A single timestamp for all grades generated in this run
  grader_timestamp = time.strftime("%Y%m%d-%H%M%S")
  jobs = [(input_path, p, grader_timestamp, api_key) for p in all_samples]

  logging.info("\nStarting grading for %d samples...", len(jobs))
  logging.info("Grader model: %s", FLAGS.model_name)

  stats = collections.Counter()
  csv_rows = []
  with concurrent.futures.ThreadPoolExecutor(
      max_workers=FLAGS.max_workers
  ) as executor:
    future_to_job = {
        executor.submit(grade_gemini_sample, *job): job for job in jobs
    }
    for future in concurrent.futures.as_completed(future_to_job):
      _, sample_path, _, _ = future_to_job[future]
      try:
        status, saved_path, csv_data = future.result()
        stats[status] += 1
        if status == "SUCCESS":
          if saved_path:
            logging.info(
                "     -> ✅ Grade saved to: %s",
                saved_path.relative_to(input_path),
            )
          if FLAGS.to_csv and csv_data:
            csv_rows.append(csv_data)

      except concurrent.futures.TimeoutError as e:
        logging.error(
            "❌ Job for '%s' timed out: %s",
            sample_path.name,
            e,
        )
        stats["FAILURE"] += 1
      except Exception as e:  # pylint: disable=broad-exception-caught
        logging.error(
            "❌ Job for '%s' generated a critical exception (%s): %s",
            sample_path.name,
            type(e).__name__,
            e,
        )
        stats["FAILURE"] += 1

  # Write to CSV if requested
  if FLAGS.to_csv and csv_rows:
    try:
      with open(FLAGS.to_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["question", "sample", "grade"])
        writer.writeheader()
        writer.writerows(csv_rows)
      logging.info("\n📝 Successfully wrote %d rows to %s", len(csv_rows), FLAGS.to_csv)
    except IOError as e:
      logging.error("\n❌ Error writing to CSV file %s: %s", FLAGS.to_csv, e)


  # Print Final Summary Report
  report = (
      f"\n{'='*40}\n"
      f"Final Grading Report\n"
      f"{'='*40}\n"
      f"  - Samples Graded: {stats['SUCCESS']}\n"
      f"  - Samples Skipped (already graded): {stats['SKIPPED']}\n"
      f"  - Samples Failed to Grade: {stats['FAILURE']}\n"
      f"{'='*40}"
  )
  print(report)


if __name__ == "__main__":
  app.run(main)
