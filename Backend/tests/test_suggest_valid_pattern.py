from unittest import TestCase
from general_utils import read_config
from Juggling.JugglingFixer import suggest_valid_pattern
from Juggling import Pattern

TEST_CONFIG = read_config("test_config")
PATTERS_CHECK = TEST_CONFIG["patterns_checks"]


class TestSuggestValidPattern(TestCase):
    def test_suggest_valid_pattern(self):
        # for siteswap, expected_problems in PATTERS_CHECK["logical_failure"].items():
        for siteswap in ["<3|3>1"]:
            pattern = Pattern(siteswap)
            fixed_pattern = suggest_valid_pattern(pattern=pattern)
            print(siteswap, fixed_pattern.siteswap)
            self.assertTrue(len(fixed_pattern.problems) == 0)
