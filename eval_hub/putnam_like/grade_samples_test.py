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

"""Tests for the Putnam-like grading pipeline."""

import pathlib
import sys
import tempfile
import types
import unittest


def _install_google_stubs() -> None:
  """Installs import-only stubs when Google API packages are unavailable."""
  try:
    import google.ai.generativelanguage  # pylint: disable=g-import-not-at-top
    import google.api_core  # pylint: disable=g-import-not-at-top
    return
  except ImportError:
    pass

  google_module = sys.modules.setdefault("google", types.ModuleType("google"))
  google_module.__path__ = []

  ai_module = types.ModuleType("google.ai")
  ai_module.__path__ = []
  glm_module = types.ModuleType("google.ai.generativelanguage")
  ai_module.generativelanguage = glm_module
  google_module.ai = ai_module
  sys.modules["google.ai"] = ai_module
  sys.modules["google.ai.generativelanguage"] = glm_module

  api_core_module = types.ModuleType("google.api_core")
  api_core_module.__path__ = []
  client_options_module = types.ModuleType("google.api_core.client_options")
  exceptions_module = types.ModuleType("google.api_core.exceptions")

  class GoogleAPICallError(Exception):
    pass

  exceptions_module.GoogleAPICallError = GoogleAPICallError
  api_core_module.client_options = client_options_module
  api_core_module.exceptions = exceptions_module
  google_module.api_core = api_core_module
  sys.modules["google.api_core"] = api_core_module
  sys.modules["google.api_core.client_options"] = client_options_module
  sys.modules["google.api_core.exceptions"] = exceptions_module


_install_google_stubs()

from eval_hub.putnam_like import grade_samples  # pylint: disable=g-import-not-at-top


class GradeSamplesTest(unittest.TestCase):

  @classmethod
  def setUpClass(cls):
    if not grade_samples.FLAGS.is_parsed():
      grade_samples.FLAGS(["grade_samples_test"])

  def setUp(self):
    grade_samples.FLAGS.model_name = "gemini-2.5-pro"

  def _make_sample(self, temp_dir: str) -> tuple[pathlib.Path, pathlib.Path]:
    input_path = pathlib.Path(temp_dir)
    sample_dir = (
        input_path / "Set_1" / "A1" / "samples" / "gemini-2-5-pro"
    )
    sample_dir.mkdir(parents=True)
    sample_path = sample_dir / "sample_001.md"
    sample_path.write_text("solution", encoding="utf-8")
    return input_path, sample_path

  def test_prior_run_grade_is_skipped(self):
    with tempfile.TemporaryDirectory() as temp_dir:
      input_path, sample_path = self._make_sample(temp_dir)
      prior_grade = (
          sample_path.parent
          / "grade_gemini-2.5-pro_20260101-000000_sample_001.json"
      )
      prior_grade.write_text("{}", encoding="utf-8")

      status, saved_path, csv_data = grade_samples.grade_gemini_sample(
          input_path,
          sample_path,
          grader_timestamp="20260822-100000",
          api_key="unused",
      )

      self.assertEqual(status, "SKIPPED")
      self.assertIsNone(saved_path)
      self.assertIsNone(csv_data)

  def test_different_grader_with_shared_prefix_is_not_skipped(self):
    with tempfile.TemporaryDirectory() as temp_dir:
      input_path, sample_path = self._make_sample(temp_dir)
      other_grade = (
          sample_path.parent
          / "grade_gemini-2.5-pro_preview_20260101-000000_sample_001.json"
      )
      other_grade.write_text("{}", encoding="utf-8")

      status, _, _ = grade_samples.grade_gemini_sample(
          input_path,
          sample_path,
          grader_timestamp="20260822-100000",
          api_key="unused",
      )

      # No question/rubric files are present, so reaching the grading path
      # returns FAILURE. The important assertion is that the other grader's
      # file did not cause an incorrect SKIPPED result.
      self.assertEqual(status, "FAILURE")


if __name__ == "__main__":
  unittest.main()
