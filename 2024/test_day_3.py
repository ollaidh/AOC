import re
from pathlib import Path

def get_muls(input: str):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)
    return matches


def calc_muls(input: str) -> list[int]:
    result = []
    muls = get_muls(input)
    for mul in muls:
        curr = int(mul[0]) * int(mul[1])
        result.append(curr)
    return result

def sum_muls(muls: list[int]) -> int:
    return sum(muls)


def test_get_muls():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    muls = get_muls(input)
    assert muls == [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]


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
