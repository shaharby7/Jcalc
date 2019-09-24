from unittest import TestCase
import re

from Juggling.BasicJuggling import Pattern
from general_utils import read_config

TEST_CONFIG = read_config("test_config")


class TestSSComposer(TestCase):
    def test_sscomposer(self):
        list_of_siteswaps = TEST_CONFIG["patterns_checks"]["success"] + list(TEST_CONFIG["patterns_checks"][
                                                                                 "logical_failure"].keys())
        siteswaps_without_inferred_passing = filter(lambda x: not re.search(r"p\D", x), list_of_siteswaps)
        for siteswap in siteswaps_without_inferred_passing:
            pattern_from_siteswap = Pattern(siteswap)
            pattern_from_beatmap = Pattern(beatmap=pattern_from_siteswap.beatmap)
            self.assertEqual(siteswap, pattern_from_beatmap.siteswap)
