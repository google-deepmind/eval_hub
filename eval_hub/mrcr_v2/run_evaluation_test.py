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

"""Tests for the MRCR V2 scoring functions."""

import sys
import types
import unittest

try:
  from eval_hub.mrcr_v2 import run_evaluation
except ImportError as error:
  if error.name not in ("google", "google.genai"):
    raise
  google_module = types.ModuleType("google")
  genai_module = types.ModuleType("google.genai")
  genai_types_module = types.ModuleType("google.genai.types")
  google_module.genai = genai_module
  genai_module.types = genai_types_module
  sys.modules["google"] = google_module
  sys.modules["google.genai"] = genai_module
  sys.modules["google.genai.types"] = genai_types_module
  from eval_hub.mrcr_v2 import run_evaluation


class MrcrV2MetricTest(unittest.TestCase):

  def setUp(self):
    self.random_hash = "AbCd1234EfGh"
    self.answer = "expected answer"
    self.target = self.random_hash + self.answer

  def test_default_metric_requires_hash_prefix(self):
    self.assertEqual(
        run_evaluation.mrcr_v2_metric(
            "preface " + self.random_hash + self.answer, self.target
        ),
        0.0,
    )

  def test_default_metric_accepts_hash_prefix(self):
    self.assertEqual(
        run_evaluation.mrcr_v2_metric(
            self.random_hash + self.answer, self.target
        ),
        1.0,
    )

  def test_lenient_metric_allows_text_before_hash(self):
    self.assertEqual(
        run_evaluation.mrcr_v2_metric_lenient(
            "preface " + self.random_hash + self.answer, self.target
        ),
        1.0,
    )

  def test_lenient_metric_uses_last_hash(self):
    prediction = (
        "preface "
        + self.random_hash
        + "wrong answer "
        + self.random_hash
        + self.answer
    )
    self.assertEqual(
        run_evaluation.mrcr_v2_metric_lenient(prediction, self.target), 1.0
    )


if __name__ == "__main__":
  unittest.main()
