import pathlib


def get_elves_from_file(filepath: str) -> list[str]:
    file = pathlib.Path(__file__).parent.resolve() / filepath
    with open(file) as f:
        lines = f.readlines()
        return lines


def calc_calories_per_elf(lines: list[str]) -> list[int]:
    calories = []
    pointer = 0
    while pointer < len(lines):
        curr_calories = 0
        while pointer < len(lines) and lines[pointer] != "\n":
            curr_calories += int(lines[pointer])
            pointer += 1
        calories.append(curr_calories)
        pointer += 1
    return calories


def calc_top_one_calories(elves_calories: list[int]) -> int:
    return max(elves_calories)


def calc_top_n_total_calories(n: int, elves_calories: list[int]) -> int:
    result = 0
    elves_calories.sort(reverse=True)
    for i in range(0, n):
        result += elves_calories[i]

    return result


def test_calories():
    # Mocking the return value of get_elves_from_file
    # fmt: off
    lines = [
        "1000", "2000", "3000", "\n",
        "4000", "\n",
        "5000", "6000", "\n",
        "7000", "8000", "9000", "\n",
        "10000"
    ]
    # fmt: on
    calories = calc_calories_per_elf(lines)
    expected_result = 24000
    assert expected_result == calc_top_one_calories(calories)


if __name__ == "__main__":
    filepath = "inputs/input_day_1.txt"
    lines = get_elves_from_file(filepath)
    calories = calc_calories_per_elf(lines)
    print(calc_top_n_total_calories(3, calories))
