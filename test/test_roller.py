import unittest
from src.roller import Roller

class TestRoller(unittest.TestCase):

    def test_roller1(self):
        """
        Test multiple die with addition
        """

        roller = Roller("2d20+5")

        self.assertEqual(roller.n, 2)
        self.assertEqual(roller.die, 20)
        self.assertEqual(roller.plus, 5)

        r = roller.roll()
        self.assertTrue(7 <= r and r <= 45)

    def test_roller2(self):

        roller = Roller("12+3")

        self.assertEqual(roller.n, 1)
        self.assertEqual(roller.die, 12)
        self.assertEqual(roller.plus, 3)
        
        r = roller.roll()
        self.assertTrue(4 <= r and r <= 15)
    
    def test_roller3(self):

        roller = Roller("6")

        self.assertEqual(roller.n, 1)
        self.assertEqual(roller.die, 6)
        self.assertEqual(roller.plus, 0)
        
        r = roller.roll()
        self.assertTrue(1 <= r and r <= 6)

