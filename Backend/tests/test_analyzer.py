from unittest import TestCase
from app import app
from general_utils import read_config
import json

TEST_CONFIG = read_config("test_config")
PATTERS_CHECK = TEST_CONFIG["patterns_checks"]
ANALYZER_PATH = "/juggling" + read_config("routes_config")["analyzer"]

MESSAGES = {
    "success": "There are problems in siteswap that should be OK. siteswap - {}",
    "logical_failure_got_success": "Siteswap {} was expected to get logical failure, but got success",
    "logical_failure_got_parsing": "Siteswap {} was expected to get logical failure, but got parsing error",
    "logical_failure_expected_problems":
        """The siteswap {} was expected to get logical failure with a specific problem, which did not happen.
        The description of the expected problem is:
        {}"""
}


class TestAnalyzer(TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def get_problems_in_siteswap(self, siteswap):
        response = self.app.post(ANALYZER_PATH, query_string={"siteswap": siteswap})
        problems = json.loads(response.json["problems"])
        return problems

    def test_analyzer_success(self):
        for siteswap in PATTERS_CHECK["success"]:
            problems = self.get_problems_in_siteswap(siteswap)
            self.assertEqual(len(problems), 0,
                             msg=MESSAGES["success"].format(siteswap))

    def test_analyzer_logical_failure(self):
        for siteswap, expected_problems in PATTERS_CHECK["logical_failure"].items():
            problems = self.get_problems_in_siteswap(siteswap)
            self.assertTrue(len(problems) > 0, msg=MESSAGES["logical_failure_got_success"].format(siteswap))
            self.assertTrue(problems[0]["kind"] != "parsing_error",
                            msg=MESSAGES["logical_failure_got_parsing"].format(siteswap))
            expected_problem_didnt_happen = None
            for expected_problem in expected_problems:
                if not TestAnalyzer.is_expected_problem_contained(expected_problem, problems):
                    expected_problem_didnt_happen = expected_problem
                    break
            self.assertTrue(expected_problem_didnt_happen is None,
                            msg=MESSAGES["logical_failure_expected_problems"].format(siteswap,
                                                                                     expected_problem_didnt_happen))

    @staticmethod
    def is_expected_problem_contained(expected_problem, all_problems):
        for problem in all_problems:
            is_that_problem_expected = True
            for expected_attribute, expected_value in expected_problem.items():
                if problem.get(expected_attribute) == expected_value:
                    continue
                else:
                    is_that_problem_expected = False
                    break
            if is_that_problem_expected:
                return True
        return False
