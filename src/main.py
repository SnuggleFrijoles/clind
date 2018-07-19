import sys
import argparse

from roll import roll

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

    args = parseArgs()

    # Check for no arguments
    if not args.roll:

        parser.print_help()
        sys.exit(1)

    # Call tool based on arguments
    if args.roll:

        die = int(args.roll[0])

        print("Rolling a d{}".format(die))

        r = roll(die)

        print(r)


if __name__ == "__main__":
    main()
