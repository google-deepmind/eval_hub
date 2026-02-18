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

r"""Basic Gemini evaluation script for LiveMath problems.

Expected Input Directory Structure (--input_dir):
└── live_math/
    └── <problem_type>/
        └── <problem_id>/
            ├── metadata.json
            ├── question/
            │   ├── question.md
            │   └── (optional images)
            └── solution/
                └── solution.md

Example usage:

export GEMINI_API_KEY=<YOUR_API_KEY>
python evaluate.py \
  --input_dir=./live_math \
  --output_dir=./live_math/results \
  --pass_at_k=1 \
  --debug_k=2

# BEGIN GOOGLE-INTERNAL
# Example with blaze run:
blaze run //third_party/eval_hub/live_math:evaluate -- \
  --input_dir=./live_math \
  --output_dir=./live_math/results \
  --pass_at_k=1 \
  --debug_k=2 \
  --alsologtostderr
# END GOOGLE-INTERNAL
"""

import collections
import concurrent.futures
import datetime
import io
import json
import os
import pathlib
import random
import re
import time
from typing import Any, Dict, Sequence

from absl import app
from absl import flags
from absl import logging
import google.ai.generativelanguage as glm
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as api_core_exceptions
import pandas as pd
from PIL import Image  # pylint: disable=g-importing-member
from PIL import UnidentifiedImageError  # pylint: disable=g-importing-member


_INPUT_DIR = flags.DEFINE_string(
    'input_dir', './live_math', 'Input directory for the final problem folders.'
)
_PASS_AT_K = flags.DEFINE_integer(
    'pass_at_k',
    1,
    'Number of samples to generate per problem for pass@k evaluation.',
)
_MAX_WORKERS = flags.DEFINE_integer(
    'max_workers', 50, 'Maximum number of parallel API requests.'
)
_DEBUG_K = flags.DEFINE_integer(
    'debug_k',
    0,
    'Run in debug mode with K problems from each category. If 0, runs on all'
    ' problems.',
)
_MULTIMODAL_DEBUG = flags.DEFINE_bool(
    'multimodal_debug',
    False,
    'Run only on multimodal problems (without images) and print details to'
    ' console for correct answers.',
)
_OUTPUT_DIR = flags.DEFINE_string(
    'output_dir', '.', 'Output directory for the results CSV file.'
)
_MODEL_NAME = flags.DEFINE_string(
    'model_name', 'gemini-2.5-pro', 'The name of the Gemini model to use.'
)
_MAX_API_RETRIES = flags.DEFINE_integer(
    'max_api_retries', 3, 'Maximum number of retries for API calls.'
)


def get_api_key() -> str | None:
  """Retrieves the Gemini API key from environment variables."""
  try:
    return os.environ['GEMINI_API_KEY']
  except KeyError:
    logging.error('❌ FATAL: GEMINI_API_KEY environment variable not found.')
    return None


def load_system_prompt() -> str:
  """Loads the system prompt from the markdown file."""
  prompt_path = pathlib.Path(__file__).parent / 'system_prompt.md'
  try:
    with open(prompt_path, 'r', encoding='utf-8') as f:
      return f.read()
  except (IOError, FileNotFoundError) as e:
    logging.error(
        '❌ FATAL: Could not load system prompt from %s: %s', prompt_path, e
    )
    return ''


def get_gemini_solution(
    problem_path: pathlib.Path,
    sample_num: int,
    multimodal_debug_flag: bool,
    system_prompt: str,
) -> Dict[str, Any]:
  """Sends one problem to Gemini, parses the response, and returns the result.

  Args:
      problem_path: Path to the problem directory.
      sample_num: The sample number for pass@k.
      multimodal_debug_flag: If True, runs in multimodal debug mode.
      system_prompt: The system prompt to use for the API call.

  Returns:
      A dictionary containing the status, parsed answer, raw answer, and
      question.
  """
  logging.info(
      '  -> Processing: %s from %s (Sample %d)',
      problem_path.name,
      problem_path.parent.name,
      sample_num,
  )
  try:
    # Load content
    question_path = problem_path / 'question' / 'question.md'
    with open(question_path, 'r', encoding='utf-8') as f:
      question = f.read()

    # Find images if they exist
    image_dir = problem_path / 'question'
    image_paths = sorted(
        list(image_dir.glob('*.png')) + list(image_dir.glob('*.jpg'))
    )
    image_parts = []
    for p in image_paths:
      try:
        with open(p, 'rb') as f:
          img = Image.open(f)
          if img:
            img.load()
            image_parts.append(img)
          else:
            logging.warning(
                'Failed to open image %s: Image.open() returned None', p
            )
      except (IOError, UnidentifiedImageError) as e:
        logging.warning('Failed to open image %s: %s', p, e)
      except Exception as e:  # pylint: disable=broad-exception-caught
        logging.warning('Unexpected error opening image %s: %s', p, e)

    # Construct the full prompt
    full_prompt = [system_prompt, '\n--- QUESTION ---\n', question]
    if image_parts and not multimodal_debug_flag:
      full_prompt.append('\n--- IMAGES ---\n')
      full_prompt.extend(image_parts)

    # Call API with retry logic
    raw_answer_text = 'API Failure'  # Default value
    parsed_number_str = ''
    for attempt in range(_MAX_API_RETRIES.value):
      try:
        api_key = get_api_key()
        if not api_key:
          raise ValueError('API key not found')
        client_options = client_options_lib.ClientOptions(api_key=api_key)
        client = glm.GenerativeServiceClient(client_options=client_options)

        parts = []
        for item in full_prompt:
          if isinstance(item, str):
            parts.append(glm.Part(text=item))
          elif isinstance(item, Image.Image):
            img_byte_arr = io.BytesIO()
            item.save(img_byte_arr, format='PNG')
            parts.append(
                glm.Part(
                    inline_data=glm.Blob(
                        mime_type='image/png', data=img_byte_arr.getvalue()
                    )
                )
            )

        response = client.generate_content(
            model=f'models/{_MODEL_NAME.value}',
            contents=[glm.Content(parts=parts)],
        )
        raw_answer_text = response.candidates[0].content.parts[0].text.strip()

        match = re.search(
            r'Final\s*answer:\s*(-?[\d\.]+)\s*$',
            raw_answer_text,
            re.IGNORECASE | re.MULTILINE,
        )
        if match:
          parsed_number_str = match.group(1)
          parsed_answer = float(parsed_number_str)
          return {
              'status': 'SUCCESS',
              'parsed_answer': parsed_answer,
              'raw_answer': raw_answer_text,
              'question': question,
          }
        else:
          logging.warning(
              "       - WARNING: Could not find ' <number>' pattern at the"
              ' end of the response on attempt %d.',
              attempt + 1,
          )
          logging.warning(
              "         - Received: '%s'...", raw_answer_text[-100:]
          )

      except (ValueError, TypeError) as e:
        logging.warning(
            "       - WARNING: Could not parse number from response '%s' on"
            ' attempt %d: %s',
            parsed_number_str,
            attempt + 1,
            e,
        )
      except api_core_exceptions.GoogleAPICallError as e:
        logging.warning(
            '       - WARNING: API call failed on attempt %d: %s',
            attempt + 1,
            e,
        )

      if attempt < _MAX_API_RETRIES.value - 1:
        time.sleep(2)
    return {
        'status': 'FAILURE',
        'parsed_answer': None,
        'raw_answer': raw_answer_text,
        'question': question,
    }

  except (IOError, FileNotFoundError) as e:
    logging.error(
        '  -> ❌ ERROR reading files for %s: %s', problem_path.name, e
    )
    return {
        'status': 'FAILURE',
        'parsed_answer': None,
        'raw_answer': 'File Read Error',
        'question': None,
    }


def main(argv: Sequence[str]) -> None:
  if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

  system_prompt = load_system_prompt()
  api_key = get_api_key()

  if not api_key or not system_prompt:
    return

  input_dir_str = _INPUT_DIR.value
  output_dir_str = _OUTPUT_DIR.value

  # Adjust paths when running with blaze run
  workspace_dir = os.environ.get('BUILD_WORKSPACE_DIRECTORY')
  if workspace_dir:
    if not os.path.isabs(input_dir_str):
      input_dir_str = os.path.join(workspace_dir, input_dir_str)
    if not os.path.isabs(output_dir_str):
      output_dir_str = os.path.join(workspace_dir, output_dir_str)

  input_path = pathlib.Path(input_dir_str)
  output_path = pathlib.Path(output_dir_str)

  if not input_path.is_dir():
    logging.error("❌ Error: Input directory '%s' not found.", input_path)
    return

  # Ensure output directory exists
  try:
    output_path.mkdir(parents=True, exist_ok=True)
    logging.info("Ensured output directory exists at '%s'", output_path)
  except OSError as e:
    logging.error(
        "❌ FATAL: Could not create output directory '%s': %s", output_path, e
    )
    return

  all_problems = []
  logging.info('Searching for problems in: %s', input_path)
  for root, _, files in os.walk(input_path):
    if 'metadata.json' in files:
      all_problems.append(pathlib.Path(root))
  all_problems.sort()

  if not all_problems:
    logging.info("No problems found in '%s'.", input_path)
    return
  else:
    logging.info("Found %d problems.", len(all_problems))

  if _MULTIMODAL_DEBUG.value:
    logging.info(
        '\n🔬 MULTIMODAL DEBUG MODE: Filtering for problems with images...'
    )
    multimodal_problems = []
    for p in all_problems:
      image_dir = p / 'question'
      if any(image_dir.glob('*.png')) or any(image_dir.glob('*.jpg')):
        multimodal_problems.append(p)

    logging.info(
        '  -> Found %d multimodal problems out of %d total.',
        len(multimodal_problems),
        len(all_problems),
    )
    all_problems = multimodal_problems

    if not all_problems:
      logging.info('No multimodal problems found to evaluate. Exiting.')
      return

  if _DEBUG_K.value > 0:
    logging.info(
        '\n🔬 DEBUG MODE: Selecting K=%d random problems from each category...',
        _DEBUG_K.value,
    )
    problems_by_category = {}
    for p in all_problems:
      category = p.parent.name
      problems_by_category.setdefault(category, []).append(p)

    debug_problems = []
    for category, problem_list in sorted(problems_by_category.items()):
      total_in_cat = len(problem_list)
      random.shuffle(problem_list)
      num_to_select = min(_DEBUG_K.value, total_in_cat)
      selected = problem_list[:num_to_select]
      debug_problems.extend(selected)
      logging.info(
          "  - Category '%s': Selected %d/%d problems.",
          category,
          len(selected),
          total_in_cat,
      )

    all_problems = debug_problems
    random.shuffle(all_problems)

  jobs = []
  for p in all_problems:
    for i in range(_PASS_AT_K.value):
      jobs.append((p, i + 1, _MULTIMODAL_DEBUG.value, system_prompt))

  logging.info(
      '\nStarting evaluation for %d problems with k=%d (Total samples: %d)...',
      len(all_problems),
      _PASS_AT_K.value,
      len(jobs),
  )

  results_by_problem = {str(p): [] for p in all_problems}
  with concurrent.futures.ThreadPoolExecutor(
      max_workers=_MAX_WORKERS.value
  ) as executor:
    future_to_job = {
        executor.submit(get_gemini_solution, *job): job for job in jobs
    }
    for future in concurrent.futures.as_completed(future_to_job):
      problem_path, _, _, _ = future_to_job[future]
      try:
        result = future.result()
        results_by_problem[str(problem_path)].append(result)
      except concurrent.futures.CancelledError as e:
        logging.warning(
            "❌ Job for '%s' was cancelled: %s", problem_path.name, e
        )
      except Exception as e:  # pylint: disable=broad-exception-caught
        logging.error(
            "❌ Job for '%s' generated an exception: %s", problem_path.name, e
        )

  # Process results and write to CSV
  output_rows = []
  category_stats = collections.Counter()
  category_correct = collections.Counter()

  for problem_path_str, results in results_by_problem.items():
    problem_path = pathlib.Path(problem_path_str)
    try:
      with open(problem_path / 'metadata.json', 'r', encoding='utf-8') as f:
        metadata = json.load(f)
      ground_truth = float(metadata.get('ANSWER'))
    except (ValueError, TypeError, FileNotFoundError) as e:
      logging.warning(
          'Skipping problem %s: Invalid or missing metadata/ground truth: %s',
          problem_path.name,
          e,
      )
      continue

    row = {
        'category': problem_path.parent.name,
        'problem_id': problem_path.name.replace('Problem_', ''),
        'ground_truth_answer': ground_truth,
    }

    correct_count = 0
    successful_samples = 0
    for i, res in enumerate(results):
      sample_idx = i + 1
      is_correct = None
      if res['status'] == 'SUCCESS' and res['parsed_answer'] is not None:
        successful_samples += 1
        is_correct = abs(res['parsed_answer'] - ground_truth) < 1e-6
        if is_correct:
          correct_count += 1
          if _MULTIMODAL_DEBUG.value and res.get('question'):
            problem_id = problem_path.name
            debug_output = (
                f'\n{"="*60}\n'
                f'✅ [MM-Debug Correct Answer] Problem: {problem_id}\n'
                f'{"="*60}\n'
                f'QUESTION: {res["question"].strip()}\n\n'
                f'CORRECT MODEL ANSWER: {res["parsed_answer"]}\n'
                f'GROUND TRUTH:         {ground_truth}\n'
                f'{"="*60}\n'
            )
            logging.info(debug_output)

      row[f'gemini_parsed_answer_{sample_idx}'] = res['parsed_answer']
      row[f'gemini_raw_answer_{sample_idx}'] = res['raw_answer']
      row[f'is_correct_{sample_idx}'] = is_correct

    row['samples_generated'] = successful_samples
    row['pass_rate'] = (
        correct_count / successful_samples if successful_samples > 0 else 0
    )
    output_rows.append(row)

    if correct_count > 0:
      category_correct[row['category']] += 1
    category_stats[row['category']] += 1

  if not output_rows:
    logging.info(
        '\nNo results were generated. Exiting without creating a CSV file.'
    )
    return

  df_output = pd.DataFrame(output_rows)
  base_cols = [
      'category',
      'problem_id',
      'ground_truth_answer',
      'samples_generated',
      'pass_rate',
  ]
  sample_cols = sorted([
      col
      for col in df_output.columns
      if col not in base_cols and 'raw_answer' not in col
  ])
  raw_cols = sorted([col for col in df_output.columns if 'raw_answer' in col])
  df_output = df_output[
      base_cols + sample_cols + raw_cols
  ]  # Move raw answers to the end

  timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
  debug_suffix = f'_DEBUG-K{_DEBUG_K.value}' if _DEBUG_K.value > 0 else ''
  multimodal_suffix = '_MM-DEBUG' if _MULTIMODAL_DEBUG.value else ''
  output_filename = f'evaluation_results_{_MODEL_NAME.value}{debug_suffix}{multimodal_suffix}_{timestamp}.csv'
  output_file = output_path / output_filename

  with open(output_file, 'w', newline='') as f:
    df_output.to_csv(f, index=False)
  logging.info("\n✅ Evaluation complete. Results saved to '%s'", output_file)

  # Print Final Summary Report
  logging.info('\n%s\nFinal Evaluation Report (pass@k)\n%s', '=' * 50, '=' * 50)
  total_problems = sum(category_stats.values())
  total_correct = sum(category_correct.values())
  for category in sorted(category_stats.keys()):
    category = str(category)
    cat_problems = category_stats[category]
    cat_correct = category_correct[category]
    cat_accuracy = (cat_correct / cat_problems * 100) if cat_problems > 0 else 0
    logging.info('  - %s:', category.title())
    logging.info(
        '    - Accuracy: %.2f%% (%d/%d problems correct)',
        cat_accuracy,
        cat_correct,
        cat_problems,
    )
  overall_accuracy = (
      (total_correct / total_problems * 100) if total_problems > 0 else 0
  )
  logging.info('-' * 25)
  logging.info(
      '  - Overall pass@%d Accuracy: %.2f%% (%d/%d problems correct)',
      _PASS_AT_K.value,
      overall_accuracy,
      total_correct,
      total_problems,
  )
  logging.info('=' * 50)


if __name__ == '__main__':
  app.run(main)
