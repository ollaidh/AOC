import re
from pathlib import Path


class SolutionPartOne:
    def __init__(self, input) -> None:
        self.input = input

    def get_muls(self):
        pattern = r"mul\((\d+),(\d+)\)"
        matches = re.findall(pattern, self.input)
        return matches
    
    def evaluate(self) -> int:
        result = 0
        muls = self.get_muls()
        for mul in muls:
            result += int(mul[0]) * int(mul[1])
        return result


class SolutionPartTwo:
    def __init__(self, input) -> None:
        self.input = input

    def parse_mul(self, mul: str) -> tuple[int, int]:
        muls = mul.rstrip(")").lstrip("mul(").split(",")
        return int(muls[0]), int(muls[1])

    def get_actions(self):
        pattern = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"
        matches = re.findall(pattern, self.input)
        return matches

    def evaluate(self) -> int:
        do = True
        result = 0
        actions = self.get_actions()
        for action in actions:
            if action.startswith("d"):
                do = "n" not in action
            elif action.startswith("m") and do  is True:
                args = self.parse_mul(action)
                result += args[0] * args[1]
        return result


def test_part1_get_muls():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    solution_part1 = SolutionPartOne(input)
    assert solution_part1.get_muls() == [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]

def test_part1_evaluate():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    solution_part1 = SolutionPartOne(input)
    assert solution_part1.evaluate() == 161

def test_part2_get_actions():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    solution_part2 = SolutionPartTwo(input)
    assert solution_part2.get_actions() == ['mul(2,4)', "don't()", 'mul(5,5)', 'mul(11,8)', 'do()', 'mul(8,5)']

def test_part2_evaluate():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    solution_part2 = SolutionPartTwo(input)
    assert solution_part2.evaluate() == 48


if __name__ == "__main__":
    filepath = Path(__file__).parent.resolve() / "inputs/input_day_3.txt"
    with open(filepath) as f:
        input = f.read()

    solution_part_1 = SolutionPartOne(input)
    result_part_1 = solution_part_1.evaluate()
    print(result_part_1)

    solution_part_2 = SolutionPartTwo(input)
    result_part_2 = solution_part_2.evaluate()
    print(result_part_2)

