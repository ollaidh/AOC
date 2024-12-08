import re
from pathlib import Path
from dataclasses import dataclass


def get_muls(input: str):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)
    return matches

def get_actions(input: str):
    pattern = r"(mul\(\d+,\d+\)|do\(\)|don't\(\))"
    matches = re.findall(pattern, input)
    return matches


def calc_muls(input: str) -> list[int]:
    result = []
    muls = get_muls(input)
    for mul in muls:
        curr = int(mul[0]) * int(mul[1])
        result.append(curr)
    return result

def parse_mul(mul: str) -> tuple[int, int]:
    muls = mul.rstrip(")").lstrip("mul(").split(",")
    return int(muls[0]), int(muls[1])


def filter_active_actions(actions: list[str]) -> int:
    do = True
    result = 0
    for action in actions:
        if action.startswith("d"):
            do = "n" not in action
        elif action.startswith("m") and do  is True:
            args = parse_mul(action)
            result += args[0] * args[1]
    return result


def sum_muls(muls: list[int]) -> int:
    return sum(muls)


def test_get_muls():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    muls = get_muls(input)
    assert muls == [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]


def test_get_actions():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert get_actions(input) == ['mul(2,4)', "don't()", 'mul(5,5)', 'mul(11,8)', 'do()', 'mul(8,5)']


def test_parse_mul():
    input = "mul(42, 24)"
    assert parse_mul(input) == (42, 24)


def test_sum_muls_actions():
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    actions = get_actions(input)
    assert filter_active_actions(actions) == 48


def test_calc_muls_result():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    muls = calc_muls(input)
    assert muls == [8, 25, 88, 40]
    result = sum_muls(muls)
    assert result == 161


if __name__ == "__main__":
    filepath = Path(__file__).parent.resolve() / "inputs/input_day_3.txt"
    with open(filepath) as f:
        input = f.read()

    muls = calc_muls(input)
    result_part_1 = sum_muls(muls)
    print(result_part_1)

    actions = get_actions(input)
    result_part_2 = filter_active_actions(actions)
    print(result_part_2)

