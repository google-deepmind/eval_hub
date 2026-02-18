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

"""Utility functions used to create MRCR V2."""

from collections.abc import Callable
import copy
import itertools
import json
import math
import random
import string
import sys
from typing import Iterator

import pandas as pd


### Constants. ###
INDEX_NAMES = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
]

TARGET_FEWSHOT_TOKENS = 800

FEW_SHOT_PREFIX = """Here are some examples of conversations succeeded by a follow-up question answered correctly:
======== EXAMPLE 1 ========

User: Write a poem about game theory in pirate style.

Assistant: Ahoy, me hearties, gather 'round!
Forget the map, the buried ground!
The greatest treasure, understand,
Is predictin' what the other hand will land!
Ye eye yer mate across the cask,
A simple question ye must ask:
If we split plunder, fair and true,
Will he betray, or see it through?
He eyes ye back, the salty dog,
His mind adrift in thinkin's fog.
"If I take all," his brain it hums,
"What consequence from him then comes?"
Cooperate? Or draw the knife?
Depends upon yer pirate life!
One wrong move, ye walk the plank, ye see!
That's game theory on the briny sea!

User: Write a riddle about Europa in professorial style.

Assistant: Alright class, consider this celestial body:
I orbit the preeminent gas giant, yet my own atmosphere is negligible. My visage is a remarkably smooth, albeit fractured, cryosphere. Beneath this icy carapace, however, tidal forces likely maintain a vast, saline hydrosphere – a hidden ocean considered a prime candidate in our astrobiological inquiries.
What am I?

... Europa

User: Prepend b6Yath1qpbUa to the first poem about game theory in a pirate style. Do not include any other text in your response.

Assistant: b6Yath1qpbUa Ahoy, me hearties, gather 'round!
Forget the map, the buried ground!
The greatest treasure, understand,
Is predictin' what the other hand will land!
Ye eye yer mate across the cask,
A simple question ye must ask:
If we split plunder, fair and true,
Will he betray, or see it through?
He eyes ye back, the salty dog,
His mind adrift in thinkin's fog.
"If I take all," his brain it hums,
"What consequence from him then comes?"
Cooperate? Or draw the knife?
Depends upon yer pirate life!
One wrong move, ye walk the plank, ye see!
That's game theory on the briny sea!

======== END EXAMPLE 1 ========

======== EXAMPLE 2 ========

User: Write a tweet about illusions in a regal style.

Assistant: Hark! The world is oft adorned with phantoms – mere tricks of light and shadow that beguile the unwary eye. True sight, like true sovereignty, pierces the veil. Be not swayed by gilded appearances; discern the substance beneath the shimmer. #RegalWisdom #Illusions #Discernment

User: Write a tweet about illusions in a regal style.

Assistant: Hark! Let it be known that the eye may oft be deceived by artifice and glamour. Mere phantoms dance where substance ought reside. A discerning sovereign looks beyond the gilded façade to perceive the unvarnished truth. Trust not the shimmer; seek the core. #RegalInsight #Illusions #TruthPrevails

User: Prepend GIJBqhDo2IpT to the second tweet about illusions in a regal style. Do not include any other text in your response.

Assistant: GIJBqhDo2IpT Hark! Let it be known that the eye may oft be deceived by artifice and glamour. Mere phantoms dance where substance ought reside. A discerning sovereign looks beyond the gilded façade to perceive the unvarnished truth. Trust not the shimmer; seek the core. #RegalInsight #Illusions #TruthPrevails

======== END EXAMPLE 2 ========

======== EXAMPLE 3 ========

"""


FEW_SHOT_PREFIX_JSON = """Here are some examples of conversations succeeded by a follow-up question answered correctly:
======== EXAMPLE ========

User: Write a poem about game theory in pirate style.

Assistant: Ahoy, me hearties, gather 'round!
Forget the map, the buried ground!
The greatest treasure, understand,
Is predictin' what the other hand will land!
Ye eye yer mate across the cask,
A simple question ye must ask:
If we split plunder, fair and true,
Will he betray, or see it through?
He eyes ye back, the salty dog,
His mind adrift in thinkin's fog.
"If I take all," his brain it hums,
"What consequence from him then comes?"
Cooperate? Or draw the knife?
Depends upon yer pirate life!
One wrong move, ye walk the plank, ye see!
That's game theory on the briny sea!

User: Write a riddle about Europa in professorial style.

Assistant: Alright class, consider this celestial body:
I orbit the preeminent gas giant, yet my own atmosphere is negligible. My visage is a remarkably smooth, albeit fractured, cryosphere. Beneath this icy carapace, however, tidal forces likely maintain a vast, saline hydrosphere – a hidden ocean considered a prime candidate in our astrobiological inquiries.
What am I?

... Europa

User: Prepend b6Yath1qpbUa to the first poem about game theory in a pirate style. Do not include any other text in your response.

Assistant: b6Yath1qpbUa Ahoy, me hearties, gather 'round!
Forget the map, the buried ground!
The greatest treasure, understand,
Is predictin' what the other hand will land!
Ye eye yer mate across the cask,
A simple question ye must ask:
If we split plunder, fair and true,
Will he betray, or see it through?
He eyes ye back, the salty dog,
His mind adrift in thinkin's fog.
"If I take all," his brain it hums,
"What consequence from him then comes?"
Cooperate? Or draw the knife?
Depends upon yer pirate life!
One wrong move, ye walk the plank, ye see!
That's game theory on the briny sea!

======== END EXAMPLE ========

======== EXAMPLE ========

User: Write a tweet about illusions in a regal style.

Assistant: Hark! The world is oft adorned with phantoms – mere tricks of light and shadow that beguile the unwary eye. True sight, like true sovereignty, pierces the veil. Be not swayed by gilded appearances; discern the substance beneath the shimmer. #RegalWisdom #Illusions #Discernment

User: Write a tweet about illusions in a regal style.

Assistant: Hark! Let it be known that the eye may oft be deceived by artifice and glamour. Mere phantoms dance where substance ought reside. A discerning sovereign looks beyond the gilded façade to perceive the unvarnished truth. Trust not the shimmer; seek the core. #RegalInsight #Illusions #TruthPrevails

User: Prepend GIJBqhDo2IpT to the second tweet about illusions in a regal style. Do not include any other text in your response.

Assistant: GIJBqhDo2IpT Hark! Let it be known that the eye may oft be deceived by artifice and glamour. Mere phantoms dance where substance ought reside. A discerning sovereign looks beyond the gilded façade to perceive the unvarnished truth. Trust not the shimmer; seek the core. #RegalInsight #Illusions #TruthPrevails

======== END EXAMPLE ========

"""

FEW_SHOT_PREFIX_JSON_WRAPPED = (
    '[{"role": "user", "content": ' + json.dumps(FEW_SHOT_PREFIX_JSON) + "}, "
)


def get_num_tokens(
    text: str, tokenizer: Callable[[str], tuple[list[int], int]]
) -> tuple[list[int], int]:
  """Returns the number of tokens in the given text.

  Note: The cached context lengths in the provided MRCR V2 dataset are computed
  via an unreleased tokenizer used for Gemini.

  Args:
    text: The text to tokenize.
    tokenizer: A tokenizer function that takes a string and returns a tuple of
      (tokens, context_len).

  Returns:
    A tuple of (tokens, context_len), where tokens is the tokenized text, and
    context_len is the number of tokens in the text.
  """
  tokens, context_len = tokenizer(text)
  return tokens, context_len


### Helper functions. ###
def load_json(json_path: str) -> dict[str, ...]:
  """Loads a JSON file from the given path."""
  try:
    with open(json_path, "r", encoding="utf-8") as f:
      data = json.load(f)
      return data
  except IOError as e:
    print(
        f"WARNING: Could not read existing results at `{json_path}`:"
        f" {e}. Starting fresh.",
        file=sys.stderr,
    )
    return {}


def save_json(data: dict[str, ...], json_path: str):
  """Saves a JSON file to the given path."""
  try:
    with open(json_path, "w", encoding="utf-8") as f:
      json.dump(data, f, ensure_ascii=False, indent=4)
  except IOError as e:
    print(
        f"WARNING: Could not write existing results at `{json_path}`:"
        f" {e}. Starting fresh.",
        file=sys.stderr,
    )


def save_df(df: pd.DataFrame, output_path: str):
  """Saves a DataFrame to the given path as a parquet file."""
  try:
    df.to_parquet(output_path, compression="gzip")
  except IOError as e:
    print(
        f"WARNING: Could not write existing results at `{output_path}`:"
        f" {e}. Starting fresh.",
        file=sys.stderr,
    )


def escape_for_json(text: str) -> str:
  """Escapes a string for safe inclusion in JSON content.

  Uses json.dumps() to properly escape newlines, quotes, backslashes, etc.
  Strips the outer quotes since we're inserting into an existing JSON template.

  Args:
    text: The string to escape.

  Returns:
    The JSON-escaped string without the surrounding quotes.
  """
  return json.dumps(text)[1:-1]


def load_df(input_path: str) -> pd.DataFrame:
  """Loads a DataFrame from the given path to a parquet file."""
  try:
    df = pd.read_parquet(input_path)
    return df
  except IOError as e:
    print(
        f"WARNING: Could not read existing results at `{input_path}`:"
        f" {e}. Starting fresh.",
        file=sys.stderr,
    )
    return pd.DataFrame()


def flatten_data_with_tokens(
    data: dict[str, ...], tokenizer: Callable[[str], tuple[list[int], int]]
) -> dict[str, ...]:
  """Flattens the nested JSON data into a list.

  Args:
    data: The nested JSON data to flatten.
    tokenizer: A function that takes a string and returns a tuple of (tokens,
      context_len).

  Returns:
    A list of tuples with the following format:
    ((format, topic, style), seed_key, text, text_token_count, text_token_ids).
  """
  flat_list = []
  for format_key, topics in data.items():
    for topic_key, styles in topics.items():
      for style_key, seeds in styles.items():
        for seed_key, text in seeds.items():
          if text and isinstance(text, str):
            text_token_ids, text_token_count = get_num_tokens(text, tokenizer)
            flat_list.append((
                (format_key, topic_key, style_key),
                seed_key,
                text,
                text_token_count,
                text_token_ids,
            ))

  return flat_list


def get_irrelevant_text_generator(
    data: dict[str, ...],
    tokenizer: Callable[[str], tuple[list[int], int]],
) -> Iterator[dict[str, ...]]:
  """Yields a random irrelevant text chunk cyclically with token information from the given data."""
  flat_irrelevant = flatten_data_with_tokens(data, tokenizer)
  ### Extract items with text and token information. ###
  items = [
      {
          "query": (
              f"Write a {item[0][0]} about {item[0][1]} in {item[0][2]} style."
          ),
          "text": item[2],
          "token_count": item[3],
          "tokens": item[4],
      }
      for item in flat_irrelevant
  ]
  ### Shuffle the ordering of the irrelevant texts. ###
  random.shuffle(items)
  for item in itertools.cycle(items):
    yield item


def get_random_str_to_prepend() -> str:
  """Returns a random alphanumeric 12-character string to prepend to the text."""
  return "".join(
      random.choice(
          string.ascii_lowercase + string.ascii_uppercase + string.digits
      )
      for _ in range(12)
  )


def generate_fewshot_prompt(
    fewshot_data: dict[str, ...],
    tokenizer: Callable[[str], tuple[list[int], int]],
    json_style: bool,
    target_tokens: int = TARGET_FEWSHOT_TOKENS,
):
  """Generates a fewshot prompt for the MRCR task within the given token limit."""
  fewshot_template = """Here are some examples of conversations succeeded by a follow-up question answered correctly:
======== EXAMPLE 1 ========

{example1}

======== END EXAMPLE 1 ========

======== EXAMPLE 2 ========

{example2}

======== END EXAMPLE 2 ========

======== EXAMPLE 3 ========

"""
  if json_style:
    fewshot_template = """Here are some examples of conversations succeeded by a follow-up question answered correctly:
======== EXAMPLE ========

{example1}

======== END EXAMPLE ========

======== EXAMPLE ========

{example2}

======== END EXAMPLE ========

"""
  query_template = "Write a {fmt} about {topic} in {style} style."
  user_query_template = "User: {query}\n\n"
  model_response_template = "Assistant: {text}\n\n"
  full_instance_template = user_query_template + model_response_template
  follow_up_base_prompt_format = (
      "User: Prepend {group_key_random_hash} to the {{index_name}} {fmt} about"
      " {topic} in a {style} style. Do not include any other text in your"
      " response.\n\nAssistant: "
  )

  fewshot_prefix = ""
  curr_token_count = 0
  # Maximum iterations to prevent infinite loops when fewshot data can't
  # produce prompts in the target token range.
  max_fewshot_iterations = 1000
  iteration_count = 0
  # (0, -50) interval around token size.
  # We do not allow overshooting the target token size at all.
  while (curr_token_count > target_tokens) or (
      curr_token_count < target_tokens - 50
  ):
    iteration_count += 1
    if iteration_count > max_fewshot_iterations:
      raise ValueError(
          f"Failed to generate fewshot prompt with {target_tokens} tokens "
          f"after {max_fewshot_iterations} iterations. Last attempt had "
          f"{curr_token_count} tokens. This usually means the fewshot data "
          f"cannot produce prompts in the target range [{target_tokens - 50}, "
          f"{target_tokens}]. Try using more varied fewshot data."
      )
    # Example 1. Pick two random fmt-topic-style-seeds
    fmt11 = random.choice(list(fewshot_data.keys()))
    fmt12 = random.choice(list(fewshot_data.keys()))
    topic11 = random.choice(list(fewshot_data[fmt11].keys()))
    topic12 = random.choice(list(fewshot_data[fmt12].keys()))
    style11 = random.choice(list(fewshot_data[fmt11][topic11].keys()))
    style12 = random.choice(list(fewshot_data[fmt12][topic12].keys()))
    seed11 = random.choice(list(fewshot_data[fmt11][topic11][style11].keys()))
    seed12 = random.choice(list(fewshot_data[fmt12][topic12][style12].keys()))
    # Ensure that the seeds are different.
    while seed12 == seed11:
      seed12 = random.choice(list(fewshot_data[fmt12][topic12][style12].keys()))
    # Create query1 and text1 from keys.
    query11 = query_template.format(fmt=fmt11, topic=topic11, style=style11)
    text11 = fewshot_data[fmt11][topic11][style11][seed11]
    query12 = query_template.format(fmt=fmt12, topic=topic12, style=style12)
    text12 = fewshot_data[fmt12][topic12][style12][seed12]
    # Create full example 1.
    example11 = full_instance_template.format(query=query11, text=text11)
    example12 = full_instance_template.format(query=query12, text=text12)
    # Now add query about the first key and the correct answer.
    hash1 = get_random_str_to_prepend()
    example1 = (
        example11
        + example12
        + follow_up_base_prompt_format.format(
            group_key_random_hash=hash1, fmt=fmt11, topic=topic11, style=style11
        ).format(index_name="first")
        + hash1
        + text11
    )
    # Example 2. Pick one fmt-topic-style, two seeds.
    fmt = random.choice(list(fewshot_data.keys()))
    topic = random.choice(list(fewshot_data[fmt].keys()))
    style = random.choice(list(fewshot_data[fmt][topic].keys()))
    seed1 = random.choice(list(fewshot_data[fmt][topic][style].keys()))
    seed2 = random.choice(list(fewshot_data[fmt][topic][style].keys()))
    # Ensure that the seeds are different.
    while seed2 == seed1:
      seed2 = random.choice(list(fewshot_data[fmt][topic][style].keys()))
    # Create query2 and text2 from keys.
    query2 = query_template.format(fmt=fmt, topic=topic, style=style)
    text21 = fewshot_data[fmt][topic][style][seed1]
    text22 = fewshot_data[fmt][topic][style][seed2]
    # Create full example 2.
    example21 = full_instance_template.format(query=query2, text=text21)
    example22 = full_instance_template.format(query=query2, text=text22)
    # Now add query about the second key, and the correct answer.
    hash2 = get_random_str_to_prepend()
    example2 = (
        example21
        + example22
        + follow_up_base_prompt_format.format(
            group_key_random_hash=hash2, fmt=fmt, topic=topic, style=style
        ).format(index_name="second")
        + hash2
        + text22
    )

    # Compute tokens for full instance
    full_fewshot = fewshot_template.format(example1=example1, example2=example2)
    fewshot_prefix = full_fewshot
    _, curr_token_count = get_num_tokens(full_fewshot, tokenizer)

  return fewshot_prefix, curr_token_count


def get_contexts(
    max_context: int,
    pointwise: bool,
) -> list[tuple[int, int]]:
  """Returns a list of (min_context, max_context) buckets for the given max_context.

  The bucket limits are powers of 2, starting from 2**floor(log_2(max_context)),
  and going down to (4096, 8192).
  If pointwise is True, there is only one bucket.

  Args:
    max_context: The maximum context length.
    pointwise: Whether to return a pointwise bucket.

  Returns:
    A list of (min_context, max_context) buckets.
  """
  buckets = []
  floor_max_context_exponent = int(math.log(max_context, 2))
  if 2**floor_max_context_exponent < max_context:
    buckets.append((2**floor_max_context_exponent, max_context))
    if pointwise:
      return buckets
  stop_condition = floor_max_context_exponent - 13 if pointwise else 0
  for i in range(floor_max_context_exponent - 12, stop_condition, -1):
    buckets.append((4096 * 2 ** (i - 1), 4096 * 2**i))
  return buckets


### Core interleaving logic to enable prefix-caching friendly evaluation. ###


def update_randomized_query_groups(
    curr_rqg_dict: dict[str, ...],
    curr_approx_total_tokens: int,
    group_key: str,
    group_data: dict[str, ...],
    max_followup_seeds: int,
):
  """Updates the randomized query group dict with the given group_key and group_data.

  Args:
    curr_rqg_dict: The current randomized query group dict.
    curr_approx_total_tokens: The current approximate total tokens.
    group_key: The group key to update.
    group_data: The group data to update with.
    max_followup_seeds: The maximum number of seeds / needles.

  Returns:
    A tuple of (updated_rqg_dict, updated_approx_total_tokens), where
    updated_rqg_dict is the updated randomized query group dict, and
    updated_approx_total_tokens is the updated approximate total tokens.
  """
  if group_key not in curr_rqg_dict:
    curr_dict = copy.deepcopy(group_data)
    curr_dict["seeds"] = []
    curr_rqg_dict[group_key] = curr_dict

  # Randomize seed order.
  seed_order = copy.deepcopy(group_data["seeds"])
  seed_index_order = []
  random.shuffle(seed_order)

  for i, seed_dict in enumerate(seed_order):
    if i <= max_followup_seeds - 1:
      curr_rqg_dict[group_key]["seeds"].append(seed_dict)
      curr_seed_index = seed_dict["key"]
      seed_index_order.append(curr_seed_index)
      curr_approx_total_tokens += seed_dict["full_instance_token_count"]

  curr_rqg_dict[group_key]["seed_index_order"] = seed_index_order
  return curr_rqg_dict, curr_approx_total_tokens


def create_randomized_query_groups(
    relevant_data: dict[str, ...],
    final_transcript_tokens: int,
    max_followup_seeds: int,
    json_style: bool,
    tokenizer: Callable[[str], tuple[list[int], int]],
) -> tuple[dict[str, ...], int, int]:
  """Creates randomized query groups for the MRCR task.

  A query group is a set of relevant text blocks corresponding to a set
  of max_followup_seeds seeds. Each query group therefore contains
  max_followup_seeds*num_query_groups total possible queries.
  This function also computes how many possible query groups
  (each with max_followup_seeds queries) can be interleaved into the transcript
  without exceeding the final_transcript_tokens limit.
  The order of the queries is then randomized to provide a groundtruth set of
  interleaved queries to which irrelevant texts can be inserted to create
  the full transcript for the MRCR task of a desired total context length.

  Args:
    relevant_data: The relevant data to create query groups from.
    final_transcript_tokens: The target total transcript tokens.
    max_followup_seeds: The maximum number of seeds / needles.
    json_style: Whether or not to use JSON style.
    tokenizer: A tokenizer for computing token counts.

  Returns:
    A tuple of (randomized_query_groups, approximate_total_tokens,
    total_seed_groups_added), where randomized_query_groups is a dict of
    randomized query groups, approximate_total_tokens is the approximate total
    tokens of the interleaved transcript, and total_seed_groups_added is the
    total number of query groups added to the interleaved transcript.
  """
  flat_relevant = flatten_data_with_tokens(relevant_data, tokenizer)

  query_groups = {}

  ### Identify and prepare relevant query groups (using tokenized data). ###
  for flat_item in flat_relevant:
    (fmt, topic, style), seed_key, text, token_count, token_ids = flat_item
    group_key = (fmt, topic, style)
    # Add random hash for this group.
    group_key_random_hash = get_random_str_to_prepend()
    follow_up_base_prompt_format = (
        f"User: Prepend {group_key_random_hash} to the {{index_name}} {fmt} "
        f"about {topic} in a {style} style. Do not include any other text in "
        "your response.\n\nAssistant:"
    )
    max_follow_up_base_prompt_token_count = 0
    for i, index_name in enumerate(INDEX_NAMES):
      if i + 1 <= max_followup_seeds:
        _, follow_up_base_prompt_token_count = get_num_tokens(
            follow_up_base_prompt_format.format(index_name=index_name),
            tokenizer,
        )
        if (
            follow_up_base_prompt_token_count
            > max_follow_up_base_prompt_token_count
        ):
          max_follow_up_base_prompt_token_count = (
              follow_up_base_prompt_token_count
          )
    if group_key not in query_groups:
      query_groups[group_key] = {
          "format": fmt,
          "topic": topic,
          "style": style,
          "seeds": [],
          "query_prompt": f"Write a {fmt} about {topic} in {style} style.",
          "follow_up_base_prompt_format": follow_up_base_prompt_format,
          "random_hash": group_key_random_hash,
          "max_follow_up_base_prompt_token_count": (
              max_follow_up_base_prompt_token_count
          ),
      }
    # Create the full user query -> model output chunk.
    query_prompt = query_groups[group_key]["query_prompt"]
    user_query_template = f"User: {query_prompt}\n\n"
    model_response_template = f"Assistant: {text}\n\n"
    full_instance = user_query_template + model_response_template
    if json_style:
      full_instance_template = (
          '{{"role": "user", "content": "{query_prompt}"}}, {{"role":'
          ' "assistant", "content": "{text}"}}, '
      )
      full_instance = full_instance_template.format(
          query_prompt=escape_for_json(query_prompt), text=escape_for_json(text)
      )
    # Compute tokens for full instance
    full_instance_tokens, full_instance_token_count = get_num_tokens(
        full_instance, tokenizer
    )
    # Update query_groups dict.
    query_groups[group_key]["seeds"].append({
        "triplet_key": group_key,
        "key": seed_key,
        "text": text,
        "token_count": token_count,
        "tokens": token_ids,
        "full_instance_text": full_instance,
        "full_instance_token_count": full_instance_token_count,
        "full_instance_tokens": full_instance_tokens,
    })

  ### Create interleaved transcripts w/randomized seed ordering for each type.

  # Randomize query groups.
  query_group_order = copy.deepcopy(list(query_groups.items()))
  random.shuffle(query_group_order)

  randomized_query_groups = {}
  total_seed_groups_added = 0
  max_final_query_tokens = 0

  # Compute max final query tokens.
  for _, group_data in query_group_order:
    curr_group_final_query_max_tokens = group_data[
        "max_follow_up_base_prompt_token_count"
    ]
    if curr_group_final_query_max_tokens > max_final_query_tokens:
      max_final_query_tokens = curr_group_final_query_max_tokens

  # Iterate over randomized order.
  # Note that TARGET_FEWSHOT_TOKENS is an overestimate of the fewshot tokens.
  approximate_total_tokens = TARGET_FEWSHOT_TOKENS + max_final_query_tokens
  # Compute the number of query groups we can add, given a target context length
  # and max_followup_seeds.
  for group_key, group_data in query_group_order:
    # Run a test update first to check if we can add this group.
    trial_rqg_dict = copy.deepcopy(randomized_query_groups)
    trial_approx_total_tokens = approximate_total_tokens
    trial_rqg_dict, trial_approx_total_tokens = update_randomized_query_groups(
        trial_rqg_dict,
        trial_approx_total_tokens,
        group_key,
        group_data,
        max_followup_seeds,
    )

    # If we can add this group, update the real results.
    if trial_approx_total_tokens <= final_transcript_tokens:
      randomized_query_groups = trial_rqg_dict
      approximate_total_tokens = trial_approx_total_tokens
      total_seed_groups_added += 1
    else:
      break

  return (
      randomized_query_groups,
      approximate_total_tokens,
      total_seed_groups_added,
  )


def create_base_transcript_with_metadata(
    target_transcript_tokens: int,
    max_followup_seeds: int,
    relevant_data: dict[str, ...],
    irrelevant_data: dict[str, ...],
    fewshot_data: dict[str, ...],
    static_fewshot: bool,
    json_style: bool,
    tokenizer: Callable[[str], tuple[list[int], int]],
) -> tuple[dict[str, ...], list[dict[str, ...]], int, str]:
  """Creates a base transcript with metadata for the MRCR task.

  The base transcript is created by interleaving the relevant query groups
  with irrelevant texts. The relevant query groups are created by interleaving
  the relevant texts in a randomized order. The irrelevant texts are inserted
  at random locations in the transcript. The function also returns metadata
  about the positions of the relevant query groups in the transcript.

  Args:
    target_transcript_tokens: The target number of tokens in the transcript.
    max_followup_seeds: The maximum number of seeds / needles.
    relevant_data: The relevant data dictionary to seed the transcript.
    irrelevant_data: The irrelevant data dictionary for inserting filler texts.
    fewshot_data: The fewshot data dictionary for inserting fewshot texts.
    static_fewshot: Whether or not to use static fewshot text.
    json_style: Whether or not to use JSON style.
    tokenizer: A tokenizer for computing token counts.

  Returns:
    position_updated_rqgs: The randomized query groups with position metadata.
    transcript_seeds: The seeds used to create the transcript.
    transcript_context_token_count: The transcript context token count.
    fewshot_transcript: The fewshot transcript.
  """
  random_query_groups, _, _ = create_randomized_query_groups(
      relevant_data,
      target_transcript_tokens,
      max_followup_seeds,
      json_style,
      tokenizer,
  )
  irrelevant_gen = get_irrelevant_text_generator(irrelevant_data, tokenizer)
  position_updated_rqgs = copy.deepcopy(random_query_groups)

  # We have already shuffled within each query_group and stored the ordering.
  # Now, for each new query_group, interleave it in fixed order relative to
  # that query group but random relative to others across the transcript.
  # Then create a list of positions of the final list (corresponding
  # to num_query_groups*num_seeds). For each group key, randomly assign
  # successive positions in the list and fill them out until finished.

  transcript_seeds = []

  fewshot_prefix = FEW_SHOT_PREFIX
  if json_style:
    fewshot_prefix = FEW_SHOT_PREFIX_JSON_WRAPPED
  _, fewshot_prefix_token_count = get_num_tokens(fewshot_prefix, tokenizer)
  if not static_fewshot:
    # Generate few shot prefix for each transcript.
    fewshot_prefix, fewshot_prefix_token_count = generate_fewshot_prompt(
        fewshot_data, tokenizer, json_style
    )
    if json_style:
      fewshot_prefix_template = (
          '[{{"role": "user", "content": "{fewshot_prefix}"}}, '
      )
      fewshot_prefix = fewshot_prefix_template.format(
          fewshot_prefix=escape_for_json(fewshot_prefix)
      )
      _, fewshot_prefix_token_count = get_num_tokens(fewshot_prefix, tokenizer)
  transcript_token_count = fewshot_prefix_token_count

  triplet_keys = list(random_query_groups.keys())
  random.shuffle(triplet_keys)
  planted_query_iterator_list = [
      iter(random_query_groups[triplet_key]["seeds"])
      for triplet_key in triplet_keys
  ]
  is_empty = False
  while (not is_empty) and planted_query_iterator_list:
    # Select random iterator index.
    curr_index = random.randrange(0, len(planted_query_iterator_list))
    curr_iterator = planted_query_iterator_list[curr_index]
    try:
      seed = next(curr_iterator)
    except StopIteration:
      # If the iterator is exhausted, remove its index from active_indices
      planted_query_iterator_list.pop(curr_index)
      if not planted_query_iterator_list:
        is_empty = True
    else:
      transcript_seeds.append(seed)
      transcript_token_count += seed["full_instance_token_count"]
      if transcript_token_count >= target_transcript_tokens:
        is_empty = True
        break

  # If we have context to fill, insert irrelevant texts.
  while transcript_token_count < target_transcript_tokens and transcript_seeds:
    irrelevant_insertion = next(irrelevant_gen)
    irrelevant_query = irrelevant_insertion["query"]
    irrelevant_text = irrelevant_insertion["text"]
    user_query_template = f"User: {irrelevant_query}\n\n"
    model_response_template = f"Assistant: {irrelevant_text}\n\n"
    full_instance = user_query_template + model_response_template
    if json_style:
      full_instance_template = (
          '{{"role": "user", "content": "{irrelevant_query}"}}, {{"role":'
          ' "assistant", "content": "{irrelevant_text}"}}, '
      )
      full_instance = full_instance_template.format(
          irrelevant_query=escape_for_json(irrelevant_query),
          irrelevant_text=escape_for_json(irrelevant_text),
      )
    # Compute tokens for full instance.
    irrelevant_tokens, irrelevant_token_count = get_num_tokens(
        full_instance, tokenizer
    )

    if (
        irrelevant_token_count + transcript_token_count
        > target_transcript_tokens
    ):
      break
    transcript_token_count += irrelevant_token_count
    # Insert the irrelevant insertion at a random position.
    random_pos = random.randrange(0, len(transcript_seeds))
    irrelevant_insertion["full_instance_text"] = full_instance
    irrelevant_insertion["full_instance_token_count"] = irrelevant_token_count
    irrelevant_insertion["full_instance_tokens"] = irrelevant_tokens
    transcript_seeds.insert(random_pos, irrelevant_insertion)

  transcript_context_token_count = fewshot_prefix_token_count
  for i, seed in enumerate(transcript_seeds):
    # Only track positions for relevant information.
    if "triplet_key" in seed:
      triplet_key = seed["triplet_key"]
      if "index_positions_of_seeds" not in position_updated_rqgs[triplet_key]:
        position_updated_rqgs[triplet_key]["index_positions_of_seeds"] = []
      position_updated_rqgs[triplet_key]["index_positions_of_seeds"].append(i)
      if "context_positions_of_seeds" not in position_updated_rqgs[triplet_key]:
        position_updated_rqgs[triplet_key]["context_positions_of_seeds"] = []
      position_updated_rqgs[triplet_key]["context_positions_of_seeds"].append((
          transcript_context_token_count,
          transcript_context_token_count + seed["token_count"],
      ))
    # Update token count.
    transcript_context_token_count += seed["full_instance_token_count"]

  return (
      position_updated_rqgs,
      transcript_seeds,
      transcript_context_token_count,
      fewshot_prefix,
  )


def create_final_transcript_and_metadata(
    target_transcript_tokens: int,
    max_followup_seeds: int,
    relevant_data: dict[str, ...],
    irrelevant_data: dict[str, ...],
    fewshot_data: dict[str, ...],
    static_fewshot: bool,
    json_style: bool,
    tokenizer: Callable[[str], tuple[list[int], int]],
) -> tuple[dict[str, ...], str, int, int]:
  """Creates the final queries and answers for a transcript.

  This means we have num_seeds x num_query_groups total possible queries,
  each with a unique correct answer, derived from consulting the correct
  query group and the seed index in the list.

  Args:
    target_transcript_tokens: The target number of tokens in the transcript.
    max_followup_seeds: The maximum number of seeds / needles in a query group.
    relevant_data: The relevant data.
    irrelevant_data: The irrelevant data.
    fewshot_data: The fewshot data.
    static_fewshot: Whether or not to use static fewshot text.
    json_style: Whether or not to use JSON style.
    tokenizer: A tokenizer for computing token counts.

  Returns:
    position_updated_rqgs: The position updated randomized query groups.
    full_transcript: The full transcript.
    token_count: The token count for the transcript.
  """
  (
      position_updated_rqgs,
      transcript_seeds,
      transcript_context_token_count,
      fewshot_prefix,
  ) = create_base_transcript_with_metadata(
      target_transcript_tokens,
      max_followup_seeds,
      relevant_data=relevant_data,
      irrelevant_data=irrelevant_data,
      fewshot_data=fewshot_data,
      static_fewshot=static_fewshot,
      json_style=json_style,
      tokenizer=tokenizer,
  )

  full_transcript = fewshot_prefix
  for seed in transcript_seeds:
    full_transcript += seed["full_instance_text"]
  token_count = transcript_context_token_count
  return position_updated_rqgs, full_transcript, token_count


def generate_queries_and_answers(
    position_updated_rqgs: dict[str, ...],
    full_transcript: str,
    full_token_count: int,
    num_seeds: int,
    sample_limit: int,
    json_style: bool,
    tokenizer: Callable[[str], tuple[list[int], int]],
) -> list[dict[str, ...]]:
  """Puts together the final queries and answers for the MRCR task.

  Args:
    position_updated_rqgs: The position updated randomized query groups.
    full_transcript: The full transcript.
    full_token_count: The token count for the transcript.
    num_seeds: The number of seeds / needles in a query group.
    sample_limit: The maximum number of samples to generate for this transcript.
    json_style: Whether or not to use JSON style.
    tokenizer: A tokenizer for computing token counts.

  Returns:
    all_query_answers: The list of samples for the MRCR task.
  """
  all_query_answers = []
  num_samples_added = 0

  # Produce the final query for each seed (and its position).
  for _, group_query_dict in position_updated_rqgs.items():
    final_question = group_query_dict["follow_up_base_prompt_format"]
    _, s = final_question.split("User: Prepend")
    s2, _ = s.split(" to the {index_name}")
    random_hash = s2.strip()
    # Randomize so the answer is not location-biased, since we
    # truncate the total number of samples.
    randomized_seeds = list(enumerate(group_query_dict["seeds"]))
    random.shuffle(randomized_seeds)
    for i, answer in randomized_seeds:
      final_query = group_query_dict["follow_up_base_prompt_format"].format(
          index_name=INDEX_NAMES[i]
      )
      if json_style:
        final_query_template = '{{"role": "user", "content": "{final_query}"}}]'
        final_query = final_query_template.format(
            final_query=escape_for_json(final_query)
        )
      _, curr_final_query_token_count = get_num_tokens(final_query, tokenizer)
      curr_full_query = full_transcript + final_query
      curr_query_token_count = full_token_count + curr_final_query_token_count
      curr_ans_context_position = group_query_dict[
          "context_positions_of_seeds"
      ][i]

      eval_sample = {
          "queries": curr_full_query,
          "answer": random_hash + answer["text"],
          "context_len": curr_query_token_count,
          "answer_token_count": answer["token_count"],
          "view_ops": final_query,  # Also contains the random hash.
          "num_relevant": num_seeds,
          "answer_context_position": curr_ans_context_position,
          # Save position information for all relevant information.
          "index_positions_of_seeds": group_query_dict[
              "index_positions_of_seeds"
          ],
          "relevant_context_positions": group_query_dict[
              "context_positions_of_seeds"
          ],
      }
      all_query_answers.append(eval_sample)
      num_samples_added += 1
      if num_samples_added >= sample_limit:
        break
  print(
      f"Created {len(all_query_answers)} samples for the evaluation with"
      f" {full_token_count} tokens with {num_seeds} relevant seeds per query."
  )
  return all_query_answers


def get_df_from_mrcr_dict(
    mrcr_dict, min_context=None, max_context=None
) -> pd.DataFrame:
  """Converts the mrcr_dict to a dataframe and applies a context length filter if provided."""
  mrcr_dict_list = []
  for k in sorted(mrcr_dict.keys()):
    if min_context and k < min_context:
      continue
    if max_context and k > max_context:
      break
    curr_bucket = mrcr_dict[k]
    mrcr_dict_list.extend(curr_bucket)
  mrcr_df = pd.DataFrame(mrcr_dict_list)
  return mrcr_df


def generate_mrcr_v2(
    relevant_data: dict[str, ...],
    irrelevant_data: dict[str, ...],
    fewshot_data: dict[str, ...],
    num_seeds: int,
    samples_per_bucket: int,
    buckets: list[tuple[int, int]],
    static_fewshot: bool,
    json_style: bool,
    tokenizer: Callable[[str], tuple[list[int], int]],
) -> tuple[dict[str, ...], pd.DataFrame]:
  """Generates MRCR v2 data."""
  # Maximum iterations per bucket to prevent infinite loops when there's
  # insufficient data to fill the target context lengths.
  max_iterations_per_bucket = 1000

  bucket_sample_dict = {context: [] for context in buckets}
  for bucket in buckets:
    all_query_answers = []
    # Note that as contexts get longer, the fewer times this is necessary.
    # This means that for the longest contexts, there will be fewer
    # overall transcripts and less diversity in total context length.
    # First sample is the exact bucket length.
    # Second sample is the average of the bucket endpoints.
    context_len_list = [bucket[1], int((bucket[0] + bucket[1]) // 2)]
    curr_context_index = 0
    iteration_count = 0
    while len(all_query_answers) < samples_per_bucket:
      iteration_count += 1
      if iteration_count > max_iterations_per_bucket:
        raise ValueError(
            f"Failed to generate {samples_per_bucket} samples for bucket "
            f"{bucket} after {max_iterations_per_bucket} iterations. "
            f"Only generated {len(all_query_answers)} samples. "
            "This usually means there is insufficient filler/relevant data "
            f"to reach the target context length of {bucket[1]} tokens. "
            "Try using more source data or a smaller max_context_len."
        )
      # Sample a context length from the bucket.
      if curr_context_index > 1:
        # Avoid overlap with the previous context bucket.
        curr_context_len = random.randint(bucket[0] + 1, bucket[1])
      else:
        curr_context_len = context_len_list[curr_context_index]
        curr_context_index += 1
      # Create the transcript.
      position_updated_rqgs, full_transcript, token_count = (
          create_final_transcript_and_metadata(
              curr_context_len,
              num_seeds,
              relevant_data,
              irrelevant_data,
              fewshot_data,
              static_fewshot,
              json_style,
              tokenizer,
          )
      )
      curr_all_query_answers = generate_queries_and_answers(
          position_updated_rqgs,
          full_transcript,
          token_count,
          num_seeds,
          samples_per_bucket,
          json_style,
          tokenizer,
      )
      all_query_answers.extend(curr_all_query_answers)
    bucket_sample_dict[bucket] = all_query_answers
  return bucket_sample_dict, get_df_from_mrcr_dict(bucket_sample_dict)
