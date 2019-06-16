import unittest
from Juggling.BasicJuggling import Pattern


class TestBasicJuggling(unittest.TestCase):

    def test_Pattern(self):
        pattern = Pattern("(4,2x)(2x,4)")
        pattern.get_landings_at_beat(4)
        print(pattern)
