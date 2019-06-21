from Juggling.JugglingDebugger.meta_functions import declare_new_pattern_validator, debug_pattern
from Juggling.JugglingDebugger.PatternProblem import PatternProblem
from Juggling.BasicJuggling import Pattern

import unittest


class TestJugglingDebugger(unittest.TestCase):
    def test_debugger(self):
        pattern = Pattern("<3p|3p>3")
        print(pattern)