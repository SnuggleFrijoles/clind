import sys
import argparse

from roller import Roller
from cli import CLI

parser = argparse.ArgumentParser()

def parseArgs():
    """
    Function: parseArgs

    Setup argument parser and execute argument parsing
    """

    args = parser.add_argument(
            "--roll", 
            nargs=1
            )

    return parser.parse_args()


def main():
    """
    Function: main

    """

    print("clind: Command Line Interface... and Dragons!")

    cli = CLI()
    cli.run()


if __name__ == "__main__":
    main()
