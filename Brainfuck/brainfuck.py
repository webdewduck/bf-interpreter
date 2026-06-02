from pathlib import Path

class Brainfuck:
    def __init__(self, file: str | Path):
        with open(file, "r") as f:
            self.code: str = f.read()
    
    def execute(self):
        cells: list[int] = [0] * 30000
        cell_index: int = 0
        instruction_index: int = 0
        while instruction_index < len(self.code):
            instruction = self.code[instruction_index]
            match instruction:
                case ">":
                    cell_index += 1
                case "<":
                    cell_index -= 1
                case "+":
                    #cells[cell_index] = (cells[cell_index] + 1) % 256
                    cells[cell_index] = clamp0_255_wraparound(cells[cell_index] + 1)
                case "-":
                    cells[cell_index] = clamp0_255_wraparound(cells[cell_index] - 1)
                case ".":
                    print(chr(cells[cell_index]), end="", flush=True)
                case ",":
                    #cells[cell_index] = ord(input()[0])
                    cells[cell_index] = clamp0_255_wraparound(int(input()))
                case "[":
                    if cells[cell_index] == 0:
                        instruction_index = self.find_bracket_match(instruction_index, True)
                case "]":
                    if cells[cell_index] != 0:
                        instruction_index = self.find_bracket_match(instruction_index, False)
            instruction_index += 1

    def find_bracket_match(self, start: int, forward: bool) -> int:
        in_between_brackets = 0
        direction = 1 if forward else -1
        location = start + direction
        start_bracket = "[" if forward else "]"
        end_bracket = "]" if forward else "["
        while 0 <= location < len(self.code):
            if self.code[location] == end_bracket:
                if in_between_brackets == 0:
                    return location
                in_between_brackets -= 1
            elif self.code[location] == start_bracket:
                in_between_brackets += 1
            location += direction
        print(f"Error: No matching bracket found for {start_bracket} at index {start}")
        return start

def clamp0_255_wraparound(value: int) -> int:
    if value < 0:
        return 255
    elif value > 255:
        return 0
    else:
        return value

    