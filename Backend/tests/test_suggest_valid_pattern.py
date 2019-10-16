from .__AppTestCase import AppTestCase
from general_utils import read_config
from functools import reduce

SUGGESTIONS_PATH = "/juggling" + read_config("routes_config")["suggest_valid_pattern"]

TEST_CONFIG = read_config("test_config")
PATTERS_CHECK = TEST_CONFIG["patterns_checks"]


class TestSuggestValidPattern(AppTestCase):
    def test_suggest_valid_pattern(self):
        for siteswap, expected_problems in PATTERS_CHECK["logical_failure"].items():
            if TestSuggestValidPattern._expected_jugglers_amount_problem(expected_problems):
                continue
            response = self.app.post(SUGGESTIONS_PATH, query_string={"siteswap": siteswap})
            if response.status_code == 200 and response.json["success"]:
                self.assertTrue(len(response.json["problems"]), 0)
            else:
                raise Exception(
                    "Jcalc should be able to suggest valid pattern to any siteswap, but {} has failed".format(siteswap))

    @staticmethod
    def _expected_jugglers_amount_problem(expected_problems):
        if not expected_problems:
            return True
        return reduce(lambda a, b: a and b,
                      [expected_problem.get("kind") == "jugglers_amount"
                       for expected_problem in expected_problems]
                      )
