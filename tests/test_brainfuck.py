import unittest 
import sys
from pathlib import Path
from io import StringIO
from Brainfuck.brainfuck import Brainfuck

def run(file:str | Path) -> str:
    output_holer = StringIO()
    sys.stdout = output_holer
    Brainfuck(file).execute()
    return output_holer.getvalue()

class TestBrainfuck(unittest.TestCase):
    def setUp(self):
        self.example_folder = (Path(__file__).resolve().parent.parent / 'Brainfuck' / "examples")
    def test_hello_world(self):
        self.assertEqual(run(self.example_folder / "hello.bf"), "Hello World!\n")

    def test_fibonacci(self):
        self.assertEqual(run(self.example_folder / "fib.bf"), "1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89")

if __name__ == "__main__":
    unittest.main()
