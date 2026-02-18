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

"""This file generates both the filler and the target texts for the MRCR task.

If run directly, it will generate the texts and save them to files
for use by generate_mrcr_task.py.
"""

import json
import os
import sys
import time

from absl import app
from absl import flags
from google import genai


FLAGS = flags.FLAGS

flags.DEFINE_boolean(
    "filler", False, "Whether to generate filler or relevant texts."
)
flags.DEFINE_boolean("fewshot", False, "Whether to generate fewshot texts.")


### Model generation details. ###
MODEL_NAME = (  # Can replace with other models as desired.
    "gemini-3-flash-preview"
)
GEMINI_API_KEY = "YOUR_API_KEY_HERE"
MODEL_CLIENT = genai.Client(api_key=GEMINI_API_KEY)

### Configuration details. ###

# Note: One can easily add more writing formats by adding them to this list.
WRITING_FORMATS = frozenset(
    ["email", "short story", "blog post", "tweet", "poem", "essay", "riddle"]
)

# Note: One can easily add more non-filler topics by adding them to this list.
TOPICS_NON_FILLER = frozenset([
    "space exploration",
    "gardening tips",
    "a fictional product launch",
    "ancient myths",
    "penguins",
    "flamingoes",
    "ducks",
])

# Note: One can easily add more filler topics by adding them to this list.
TOPICS_FILLER = frozenset([
    "black holes",
    "dreams",
    "Cambrian Explosion",
    "The Renaissance",
    "sign language",
    "dystopia",
])

# Note: One can easily add more fewshot topics by adding them to this list.
TOPICS_FEWSHOT = frozenset([
    "game theory",
    "Europa",
    "illusions",
    "lost languages",
    "fractals",
    "The Myth of Sisyphus",
    "lions",
])

# Note: One can easily add more styles by adding them to this list.
STYLES = frozenset([
    "formal",
    "informal",
    "humorous",
    "technical",
    "archaic",
])

# Note: One can easily add more styles for fewshot by adding them to this list.
STYLES_FEWSHOT = frozenset([
    "pirate",
    "professorial",
    "regal",
    "journalistic",
    "hard-boiled",
    "gothic",
])

# Note: One can easily add more tweaks by adding them to this list.
# The tweaks serve to add sufficient variety to the different instances
# of the same {format} on {topic} in {style}.
# Here we support 8 different seeds which corresponds to the maximum of 8
# needles. We can easily add more seeds by adding more keys to this dictionary.
TWEAK_DICT = {
    "seed1": "as if explaining it to a child.",
    "seed2": "with a focus on future possibilities.",
    "seed3": "starting with a compelling question.",
    "seed4": "emphasizing the potential challenges.",
    "seed5": "from the perspective of an excited beginner.",
    "seed6": "as if rallying troops before a battle.",
    "seed7": "as if writing a secret memo only for insiders.",
    "seed8": "as if explaining it to a skeptical investor.",
}

### Constants. ###
NUM_SEEDS_PER_COMBINATION = 8
API_DELAY_SECONDS = 0.1
ERROR_PREFIX = "ERROR: Failed to generate"


### File paths ###
CURR_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(CURR_DIR, "mrcr_text_blocks/")
RELEVANT_OUTPUT_FILENAME = "mrcr_relevant_texts.json"
FILLER_OUTPUT_FILENAME = "mrcr_filler_texts.json"
FEWSHOT_OUTPUT_FILENAME = "mrcr_fewshot_texts.json"


##### Functions for loading and saving files robustly. #####
def load_results(filename: str):
  """Loads the results from the given JSON filename."""
  if not os.path.exists(filename):
    print(f"No existing results found at `{filename}`. Starting fresh.")
    return {}
  try:
    with open(filename, "r", encoding="utf-8") as f:
      data = json.load(f)
      print(f"Successfully loaded existing results from `{filename}`.")
      return data
  except json.JSONDecodeError as e:
    print(
        f"WARNING: Could not decode JSON from existing results at `{filename}`:"
        f" {e}. Starting fresh.",
        file=sys.stderr,
    )
    return {}
  except IOError as e:
    print(
        f"WARNING: Could not read existing results at `{filename}`:"
        f" {e}. Starting fresh.",
        file=sys.stderr,
    )
    return {}


def save_results_robustly(
    data: dict[str, dict[str, dict[str, dict[str, str]]]],
    final_filename: str,
    temp_filename: str,
):
  """Saves the dictionary data robustly to a temporary file."""
  if not os.path.exists(os.path.dirname(final_filename)):
    os.makedirs(os.path.dirname(final_filename), exist_ok=True)
  try:
    with open(temp_filename, "w", encoding="utf-8") as f:
      json.dump(data, f, ensure_ascii=False, indent=4)
    os.replace(temp_filename, final_filename)
    print(f"Successfully saved results to `{final_filename}`.")
  except IOError as e:
    print(
        f"ERROR: Failed to save results to `{final_filename}` "
        f"via temporary file: {e}.",
        file=sys.stderr,
    )
  except TypeError as e:
    print(
        f"ERROR: Could not serialize data to JSON: {e}.",
        file=sys.stderr,
    )


##### Functions for generating the filler and target texts. #####
def get_llm_response(text_prompt: str) -> str:
  """Returns the LLM response to the given text prompt."""
  response = MODEL_CLIENT.models.generate_content(
      model=MODEL_NAME,
      contents=[text_prompt],
  )
  return response.text


def is_valid_generation(text: str, error_prefix: str) -> bool:
  """Returns True if the LLM response is valid, False otherwise."""
  if not isinstance(text, str):
    return False
  if text.strip().startswith(error_prefix):
    return False
  return True


def generate_writings(
    num_seeds: int,
    existing_results: dict[str, dict[str, dict[str, dict[str, str]]]],
    error_prefix: str,
    is_filler: bool,
    is_fewshot: bool,
) -> dict[str, dict[str, dict[str, dict[str, str]]]]:
  """Generates MRCR texts (formats, topics, and styles) for num_seeds seeds.

  We load the existing results from the existing_results dictionary, skipping
  valid previously completed seeds, regenerating seeds marked with error_prefix,
  and update the results dictionary with the newly generated seeds robustly.

  Args:
    num_seeds: The number of seeds to generate for each format, topic, and style
      combination.
    existing_results: The existing results dictionary.
    error_prefix: The error prefix to check for in the existing results.
    is_filler: Whether to generate filler or relevant texts.
    is_fewshot: Whether to generate fewshot texts.

  Returns:
    The updated results dictionary with the newly generated seeds.
  """
  formats = WRITING_FORMATS
  topics = TOPICS_FILLER if is_filler else TOPICS_NON_FILLER
  # If generating fewshot texts, override the filler and relevant logic.
  if is_fewshot:
    topics = TOPICS_FEWSHOT
  styles = STYLES if not is_fewshot else STYLES_FEWSHOT
  output_filename = (
      FILLER_OUTPUT_FILENAME if is_filler else RELEVANT_OUTPUT_FILENAME
  )
  if is_fewshot:
    output_filename = FEWSHOT_OUTPUT_FILENAME
  output_filename = os.path.join(OUTPUT_DIR, output_filename)
  temp_output_filename = f"{output_filename}.tmp"

  results = existing_results
  total_combinations = len(formats) * len(topics) * len(styles)

  print("Starting generation/verification...")
  print(f"Target seeds per combination: {num_seeds}")
  print(f"Checking {total_combinations} combinations...")
  print(f"Total seeds to generate: {total_combinations * num_seeds}")
  print(f"Will regenerate seeds starting with `{error_prefix}`.")
  print("-" * 30)

  generated_this_run = 0
  regenerated_this_run = 0
  skipped_valid = 0
  processed_triplets = 0
  for fmt in formats:
    results.setdefault(fmt, {})
    for topic in topics:
      results[fmt].setdefault(topic, {})
      for style in styles:
        results[fmt][topic].setdefault(style, {})

        processed_triplets += 1
        progress_prefix = (
            f"[{processed_triplets}/{total_combinations}] ({fmt}, {topic},"
            f" {style})"
        )

        style_results = results[fmt][topic][style]
        seeds_to_generate_for_triplet = []
        valid_seeds_found = 0

        # Check the seeds for this triplet.
        for seed_index in range(num_seeds):
          seed_key = f"seed{seed_index+1}"
          existing_value = style_results.get(seed_key, None)
          if is_valid_generation(existing_value, error_prefix):
            valid_seeds_found += 1
            skipped_valid += 1
          else:
            if existing_value is not None:  # It exists but is invalid error.
              print(
                  f"{progress_prefix}: Found previous error for {seed_key}."
                  " Regenerating."
              )
            seeds_to_generate_for_triplet.append(seed_key)

        if not seeds_to_generate_for_triplet:
          print(f"{progress_prefix}: All seeds are valid. Skipping.")
          continue  # Move to the next style if all seeds are valid.

        print(
            f"{progress_prefix}: Found {valid_seeds_found} valid seeds. Needs"
            f" {len(seeds_to_generate_for_triplet)} more seeds."
        )

        # Generate/re-generate the required seeds for this triplet.
        for seed_key in seeds_to_generate_for_triplet:
          is_regeneration = (
              seed_key in style_results
          )  # Are we overwriting an existing seed?
          action_str = "Regenerating" if is_regeneration else "Generating"
          print(f"  - {action_str} {seed_key}...")
          sys.stdout.flush()

          prompt = (
              f"Please write a piece of text in the format of a `{fmt}`.\n"
              f"The topic should be: `{topic}`.\n"
              f"The writing style should be: `{style}`.\n\n"
              f"Apply this specific variation: {TWEAK_DICT[seed_key]}\n\n"
              "Generate only the text content itself."
          )

          try:
            # Get the LLM response.
            generated_text = get_llm_response(prompt)
            style_results[seed_key] = generated_text
            if is_regeneration:
              regenerated_this_run += 1
            else:
              generated_this_run += 1

            if API_DELAY_SECONDS > 0:
              time.sleep(API_DELAY_SECONDS)

          except Exception as e:  # pylint: disable=broad-except
            error_message = (
                f"{error_prefix} {seed_key} - {type(e).__name__}: {e}"
            )
            print(f"\n !!! {error_message}", file=sys.stderr)
            style_results[seed_key] = error_message  # Store the error message.
            time.sleep(max(API_DELAY_SECONDS, 0.5))  # Pause longer after error.

        # Save after processing all seeds for this triplet.
        print(
            f"{progress_prefix}: Finished processing triplet. Saving results..."
        )
        save_results_robustly(
            results,
            final_filename=output_filename,
            temp_filename=temp_output_filename,
        )

  print("-" * 30)
  print("Generation loop finished.")
  print(f"Generated {generated_this_run} new seeds this run.")
  print(f"Regenerated {regenerated_this_run} seeds from previous errors.")
  print(f"Skipped {skipped_valid} already valid seeds.")
  print("-" * 30)
  print("Performing final save...")
  save_results_robustly(
      results,
      final_filename=output_filename,
      temp_filename=temp_output_filename,
  )
  print("All done.")
  return results


# Usage: pass in --filler to generate the filler texts, or --fewshot to
# generate the fewshot texts. Otherwise, generates relevant texts.
def main(argv) -> None:
  del argv  # Unused by main, flags are accessed via FLAGS.

  print_text = "filler" if FLAGS.filler else "relevant"
  output_file = (
      FILLER_OUTPUT_FILENAME if FLAGS.filler else RELEVANT_OUTPUT_FILENAME
  )
  # If generating fewshot texts, override the other flag.
  if FLAGS.fewshot:
    print_text = "fewshot"
    output_file = FEWSHOT_OUTPUT_FILENAME

  output_file = os.path.join(OUTPUT_DIR, output_file)
  print(f"Loading existing {print_text} results...")
  existing_results = load_results(output_file)

  ### Generate the MRCR texts. ###
  print(f"Generating {print_text} texts...")
  generate_writings(
      num_seeds=NUM_SEEDS_PER_COMBINATION,
      existing_results=existing_results,
      error_prefix=ERROR_PREFIX,
      is_filler=FLAGS.filler,
      is_fewshot=FLAGS.fewshot,
  )


if __name__ == "__main__":
  app.run(main)
