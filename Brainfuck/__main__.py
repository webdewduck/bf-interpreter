from argparse import ArgumentParser
from Brainfuck.brainfuck import Brainfuck

if __name__ == "__main__":
    file_parser = ArgumentParser("Brainfuck")
    file_parser.add_argument("brainfuck_file", help="The brainfuck file to execute")

    args = file_parser.parse_args()
    Brainfuck(args.brainfuck_file).execute()
