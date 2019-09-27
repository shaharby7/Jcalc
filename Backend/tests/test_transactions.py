from .__AppTestCase import AppTestCase
from general_utils import read_config

TRANSACTIONS_PATH = "/juggling" + read_config("routes_config")["transactions"]

TEST_CONFIG = read_config("test_config")
TRANSACTIONS_CHECKS = TEST_CONFIG["transactions_checks"]


class TestTransactions(AppTestCase):
    def test_transactions(self):
        for siteswap1, siteswap2 in TRANSACTIONS_CHECKS:
            response = self.app.post(TRANSACTIONS_PATH,
                                     query_string={"siteswap_1": siteswap1, "siteswap_2": siteswap2})
            if response.status_code == 200:
                self.assertTrue(len(response.json["problems"]), 0)
                self.assertTrue(siteswap1 in response.json["siteswap"])
                self.assertTrue(siteswap2 in response.json["siteswap"])
                print(siteswap1, siteswap2, response.json["siteswap"])
            elif response.status_code == 500:
                self.assertTrue(response.json["error_type"] == "JugglingException")
                print(siteswap1, siteswap2, "failed")
            else:
                raise Exception("Application failed without JugglingException")
