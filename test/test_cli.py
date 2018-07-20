import unittest
from src.cli import CLI
from src.exceptions import *

class TestCLI(unittest.TestCase):

    def testProcessCommand(self):

        cli = CLI()
        
        # Check for incorrect command
        with self.assertRaises(ClindException):
            
            cli.processCommand("not a command")
        
        # Check roll command
        for i in range(100):

            r = cli.processCommand("roll 1d20")

            self.assertTrue(1 <= r <= 20)


