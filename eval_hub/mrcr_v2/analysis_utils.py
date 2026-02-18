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

"""Analysis utils for MRCR V2.

A set of functions to help analyze the distribution of the MRCR V2 queries.
"""

import difflib
import math
import re

import matplotlib.pyplot as plt
import pandas as pd


def to_tuple(fake_tuple: str) -> tuple[int, ...]:
  """Converts a string description of a tuple of ints to a tuple of ints."""
  if isinstance(fake_tuple, tuple):
    return fake_tuple
  # Handle numpy arrays
  if hasattr(fake_tuple, "tolist"):
    return tuple(fake_tuple.tolist())
  return tuple(int(x) for x in fake_tuple.strip(")").strip("(").split(","))


def to_list(fake_list_of_tuples: str) -> list[tuple[int, ...]]:
  """Converts a string description of a list of tuples of ints to a list of tuples of ints."""
  if isinstance(fake_list_of_tuples, list):
    return fake_list_of_tuples
  # Handle numpy arrays (e.g., array of arrays)
  if hasattr(fake_list_of_tuples, "tolist"):
    return [
        tuple(item) if hasattr(item, "__iter__") else (item,)
        for item in fake_list_of_tuples.tolist()
    ]
  return [
      to_tuple(fake_tuple.strip())
      for fake_tuple in fake_list_of_tuples.strip("[").strip("]").split("),")
  ]


number_to_index_dict = {
    "first": 0,
    "second": 1,
    "third": 2,
    "fourth": 3,
    "fifth": 4,
    "sixth": 5,
    "seventh": 6,
    "eighth": 7,
}


def get_final_q(mrcr_example):
  user_query = mrcr_example["view_ops"]
  user_query = user_query.split("Prepend")[1]
  random_string = user_query.split("to ")[0].strip()
  rest = user_query.split(f"{random_string} to the")[1].lstrip()
  index = rest.split(" ")[0]
  index_int = number_to_index_dict[index]
  query = rest.split(".")[0].lstrip(index).strip()
  return {
      "random_string": random_string,
      "index": index_int,
      "query": query.replace("in a", "in"),
  }


def find_copies_of_query_string(query_str, mrcr_example):
  context = mrcr_example["queries"]
  search_str = f"User: Write a {query_str}.\n\nAssistant:"
  instances = [m.start() for m in re.finditer(re.escape(search_str), context)]
  str_instances = [
      context[i:].split("\n\nUser:")[0].split("\n\nAssistant:")[1].strip()
      for i in instances
  ]
  return str_instances


def are_answers_different(mrcr_example):
  final_q_dict = get_final_q(mrcr_example)
  final_q = final_q_dict["query"]
  instances = find_copies_of_query_string(final_q, mrcr_example)
  if not instances:
    return False
  for i, instance in enumerate(instances):
    # Check if instance is equal to any before it.
    for j in range(i):
      if instance == instances[j]:
        return False
  return True


def is_correct_num_needles(mrcr_example, true_num_needles):
  final_q_dict = get_final_q(mrcr_example)
  final_q = final_q_dict["query"]
  instances = find_copies_of_query_string(final_q, mrcr_example)
  return len(instances) == true_num_needles


def is_final_query_in_context(mrcr_example):
  final_q = mrcr_example["view_ops"]
  context = mrcr_example["queries"]
  return final_q in context


def solve_mrcr_example(mrcr_example):
  final_q_dict = get_final_q(mrcr_example)
  final_q = final_q_dict["query"]
  random_string = final_q_dict["random_string"]
  index = final_q_dict["index"]
  instances = find_copies_of_query_string(final_q, mrcr_example)
  correct_instance = instances[index]
  recorded_answer = mrcr_example["answer"].strip()
  derived_answer = random_string.strip() + correct_instance.strip()
  return int(recorded_answer == derived_answer)


def compute_seqmatch_ratio(target, prediction):
  d = difflib.SequenceMatcher(a=target, b=prediction)
  return d.ratio()


def get_all_assistant_replies(mrcr_example):
  context = mrcr_example["queries"]
  search_str = "\n\nAssistant:"
  instances = [m.start() for m in re.finditer(re.escape(search_str), context)]
  str_instances = [
      context[i:].split("\n\nUser:")[0].split("\n\nAssistant:")[1].strip()
      for i in instances
  ]
  return str_instances


def compute_noise_rate_example(
    mrcr_example, uniform_all_or_uniform_relevant="relevant"
):
  """Computes a noise rate for a single MRCR example.

  The noise rate is calculated as the average SequenceMatcher ratio between the
  correct assistant reply and other assistant replies in the context.

  Args:
    mrcr_example: A single MRCR example.
    uniform_all_or_uniform_relevant: Specifies whether to compute noise relative
      to all assistant replies ("all") or only relevant ones ("relevant").

  Returns:
    The average SequenceMatcher ratio, representing the noise rate.

  Raises:
    ValueError: If uniform_all_or_uniform_relevant is not "all" or "relevant".
  """
  final_q_dict = get_final_q(mrcr_example)
  final_q = final_q_dict["query"]
  index = final_q_dict["index"]
  relevant_instances = find_copies_of_query_string(final_q, mrcr_example)
  correct_instance = relevant_instances[index]
  if uniform_all_or_uniform_relevant == "all":
    all_instances = get_all_assistant_replies(mrcr_example)
    avg_ratio = sum(
        compute_seqmatch_ratio(correct_instance, instance)
        for instance in all_instances
    ) / len(all_instances)
    return avg_ratio
  elif uniform_all_or_uniform_relevant == "relevant":
    avg_ratio = sum(
        compute_seqmatch_ratio(correct_instance, instance)
        for instance in relevant_instances
    ) / len(relevant_instances)
    return avg_ratio
  else:
    raise ValueError(
        "Invalid value for uniform_all_or_uniform_relevant:"
        f" {uniform_all_or_uniform_relevant}"
    )


def compute_noise_rate_dataset(
    mrcr_dataset, uniform_all_or_uniform_relevant="relevant"
):
  """Computes the average noise rate across a dataset of MRCR examples.

  The noise rate is calculated based on the similarity of assistant replies.

  Args:
    mrcr_dataset: A pandas DataFrame containing MRCR examples.
    uniform_all_or_uniform_relevant: Specifies whether to compute noise relative
      to all assistant replies ("all") or only relevant ones ("relevant").

  Returns:
    A tuple containing:
      - noises: A list of noise rates for each example in the dataset.
      - avg_noise: The average noise rate across the dataset.
  """
  noises = []
  avg_noise = 0
  for i in range(len(mrcr_dataset)):
    curr_mrcr_example = mrcr_dataset.iloc[i]
    example_noise_rate = compute_noise_rate_example(
        curr_mrcr_example, uniform_all_or_uniform_relevant
    )
    noises.append(example_noise_rate)
    avg_noise += example_noise_rate
  avg_noise /= len(mrcr_dataset)
  _ = plt.hist(noises)
  print(f"Avg. {uniform_all_or_uniform_relevant} noise rate: {100*avg_noise}%")
  return noises, avg_noise


def run_mrcr_tests(mrcr_dataset, true_num_needles):
  """Runs a series of tests on the MRCR dataset and prints the results.

  Specifically, it computes and prints:
  - The accuracy of `solve_mrcr_example`.
  - Whether all examples have different answers for copied queries.
  - Whether the final query is present in the context for all examples.
  - Whether all examples contain the correct number of "needles" (copied
  queries).

  Args:
    mrcr_dataset: A pandas DataFrame containing MRCR examples.
    true_num_needles: The expected number of times the final query appears as a
      "needle" in the context.
  """
  accuracy = 0
  all_ans_diff = True
  all_is_final_query_in_context = True
  all_is_correct_num_needles = True
  for i in range(len(mrcr_dataset)):
    curr_mrcr_example = mrcr_dataset.iloc[i]
    accuracy += solve_mrcr_example(curr_mrcr_example)
    all_ans_diff = all_ans_diff and are_answers_different(curr_mrcr_example)
    all_is_final_query_in_context = (
        all_is_final_query_in_context
        and is_final_query_in_context(curr_mrcr_example)
    )
    all_is_correct_num_needles = (
        all_is_correct_num_needles
        and is_correct_num_needles(curr_mrcr_example, true_num_needles)
    )
  print(f"Accuracy: {100*accuracy/len(mrcr_dataset)}%")
  print(f"All answers different: {all_ans_diff}")
  print(f"All final queries in context: {all_is_final_query_in_context}")
  print(f"All correct number of needles: {all_is_correct_num_needles}")


def analyze_mrcr_v2_eval_df(df: pd.DataFrame) -> None:
  """Analyzes the MRCR V2 eval dataframe and plots the distributions.

  Plots the distributions of the context length, answer context start, answer
  context end, relevant context start, and relevant context end.
  The relevant information is normalized by the total context length.

  Args:
    df: The MRCR V2 eval dataframe.
  """

  # Bucket the context lengths into powers of 2.
  context_bucket_dict = {
      (4096 * 2**i, 4096 * 2 ** (i + 1)): 0 for i in range(11)
  }
  total_samples = len(df)
  max_context = 0
  min_context = math.inf
  max_output = 0
  contexts = []
  answer_context_starts = []
  answer_context_ends = []
  relevant_context_starts = []
  relevant_context_ends = []
  normalized_answer_context_starts = []
  normalized_answer_context_ends = []
  normalized_relevant_context_starts = []
  normalized_relevant_context_ends = []
  unique_fewshots = set()
  for _, row in df.iterrows():
    query = row["queries"]
    fewshot_portion = query.split("======== EXAMPLE 3 ========")[0]
    unique_fewshots.add(fewshot_portion)
    curr_context = row["context_len"]
    contexts.append(curr_context)
    if curr_context > max_context:
      max_context = curr_context
    if curr_context < min_context:
      min_context = curr_context
    for bucket in context_bucket_dict.keys():
      if bucket[0] <= curr_context <= bucket[1]:
        context_bucket_dict[bucket] += 1
        break
    curr_output = row["answer_token_count"]
    if curr_output > max_output:
      max_output = curr_output
    answer_context_starts.append(to_tuple(row["answer_context_position"])[0])
    normalized_answer_context_starts.append(
        to_tuple(row["answer_context_position"])[0] / curr_context
    )
    answer_context_ends.append(to_tuple(row["answer_context_position"])[1])
    normalized_answer_context_ends.append(
        to_tuple(row["answer_context_position"])[1] / curr_context
    )
    for rel_context in to_list(row["relevant_context_positions"]):
      relevant_context_starts.append(rel_context[0])
      normalized_relevant_context_starts.append(rel_context[0] / curr_context)
      relevant_context_ends.append(rel_context[1])
      normalized_relevant_context_ends.append(rel_context[1] / curr_context)

  print(f"Total Samples: {total_samples}")
  print(f"Max Context: {max_context}")
  print(f"Min Context: {min_context}")
  print(f"Max Output: {max_output}")
  print("Number of unique fewshots: ", len(unique_fewshots))
  print(f"Context Buckets: {context_bucket_dict}")
  plt.hist(contexts, bins=100)
  plt.title("Context Length Distribution")
  plt.show()

  plt.hist(normalized_answer_context_starts, bins=100)
  plt.title("Normalized Answer Context Start Distribution")
  plt.show()

  plt.hist(normalized_answer_context_ends, bins=100)
  plt.title("Normalized Answer Context End Distribution")
  plt.show()

  plt.hist(normalized_relevant_context_starts, bins=100)
  plt.title("Normalized Relevant Context Start Distribution")
  plt.show()

  plt.hist(normalized_relevant_context_ends, bins=100)
  plt.title("Normalized Relevant Context End Distribution")
  plt.show()

  return
