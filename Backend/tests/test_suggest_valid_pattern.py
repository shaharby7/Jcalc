from .__AppTestCase import AppTestCase
from general_utils import read_config

SUGGESTIONS_PATH = "/juggling" + read_config("routes_config")["suggest_valid_pattern"]

TEST_CONFIG = read_config("test_config")
PATTERS_CHECK = TEST_CONFIG["patterns_checks"]


class TestSuggestValidPattern(AppTestCase):
    def test_suggest_valid_pattern(self):
        for siteswap, expected_problems in PATTERS_CHECK["logical_failure"].items():
            response = self.app.post(SUGGESTIONS_PATH, query_string={"siteswap": siteswap})
            if response.status_code == 200:
                self.assertTrue(len(response.json["problems"]), 0)
                # print(siteswap, response.json["siteswap"])
            elif response.status_code == 500:
                self.assertTrue(response.json["error_type"] == "JugglingException")
                # print(siteswap, "failed")
            else:
                raise Exception("Application failed without JugglingException")
