import unittest
from Juggling.BasicJuggling import Pattern


class TestBasicJuggling(unittest.TestCase):

    def test_Pattern(self):
        pattern = Pattern("123")
        pattern._calculate_catches_at_beat(4)
        print(pattern)
