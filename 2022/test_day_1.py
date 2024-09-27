import pathlib
import unittest
from unittest.mock import patch


def calc_max_calories(lines: list[str]) -> int:
    calories = []
    pointer = 0
    while pointer < len(lines):
        curr_calories = 0
        while pointer < len(lines) and lines[pointer] != "\n":
            curr_calories += int(lines[pointer])
            pointer += 1
        calories.append(curr_calories)
        pointer += 1
    return max(calories)


def get_elves_from_file(filepath: str) -> list[str]:
    file = pathlib.Path(__file__).parent.resolve() / filepath
    with open(file) as f:
        lines = f.readlines()
        return lines


def test_calories():
    # Mocking the return value of get_elves_from_file
    lines = [
        "1000", "2000", "3000", "\n",
        "4000", "\n",
        "5000", "6000", "\n",
        "7000", "8000", "9000", "\n",
        "10000"
    ]
    expected_result = 24000
    assert expected_result == calc_max_calories(lines)


if __name__ == "__main__":
    lines = get_elves_from_file(filepath)
    print(calc_max_calories(lines))

