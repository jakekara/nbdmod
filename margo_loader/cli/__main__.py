import argparse
from margo_parser import parser
from .commands import extract


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subcommand")

    extract.register(subparsers)

    args = parser.parse_args()
    if args.subcommand == "extract":
        extract.main(args)


if __name__ == "__main__":
    main()
