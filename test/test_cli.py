import unittest

import sys

sys.path.append("src")

from cli import CLI
from exceptions import *

class TestCLI(unittest.TestCase):
    """
    class: TestCLI

    Test cases for the CLI class
    """

    def testInvalidCommand(self):

        cli = CLI()
        
        # Check for incorrect command
        with self.assertRaises(ClindException):
            
            cli.processCommand("not a command")
      

    def testRoll(self):

        cli = CLI()

        # Check roll command
        for i in range(100):

            r = cli.processCommand("roll 1d20")

            self.assertTrue(1 <= r <= 20)


    def testName(self):

        cli = CLI()
        
        name = cli.processCommand("name")
        
        # Check that name command returns a string with space
        self.assertTrue(isinstance(name, str))
        self.assertTrue(" " in name)


