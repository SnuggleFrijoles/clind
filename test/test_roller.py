import unittest
from ..src.roller import Roller

class TestRoller(unittest.TestCase):

    def test_roller(self):

        roller = Roller("2d20+5")

        self.assertEqual(roller.n, 2)
        self.assertEqual(roller.die, 20)
        self.assertEqual(roller.plus, 5)


