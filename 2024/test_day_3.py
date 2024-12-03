import re
from pathlib import Path

def get_muls(input: str):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)
    return matches


def calc_muls_result(input: str) -> dict:
    result: dict = {}
    result["result"] = 0
    result["mults_results"] = []
    muls = get_muls(input)
    for mul in muls:
        curr = int(mul[0]) * int(mul[1])
        result["result"] += curr
        result["mults_results"].append(curr)
    return result


def test_get_muls():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    muls = get_muls(input)
    assert muls == [('2', '4'), ('5', '5'), ('11', '8'), ('8', '5')]


def test_calc_muls_result():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    result = calc_muls_result(input)
    assert result["result"] == 161
    assert result["mults_results"] == [8, 25, 88, 40]


if __name__ == "__main__":
    filepath = Path(__file__).parent.resolve() / "inputs/input_day_3.txt"
    with open(filepath) as f:
        input = f.read()
    result_part_1 = calc_muls_result(input)["result"]
    print(result_part_1)
