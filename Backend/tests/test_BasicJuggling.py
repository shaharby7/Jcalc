import unittest
from BasicJuggling import Pattern


class TestBasicJuggling(unittest.TestCase):

    def test_Pattern(self):
        pattern = Pattern("<2|2p|2p1>")
        print(pattern)
