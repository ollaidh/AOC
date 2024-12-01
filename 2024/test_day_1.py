from pathlib import Path

def calc_distance(locations_1: list[int], locations_2: list[int]) -> int:
    locations_1.sort()
    locations_2.sort()
    total_distance = 0
    for loc_1, loc_2 in zip(locations_1, locations_2):
        total_distance += abs(loc_1 - loc_2)
    return total_distance


def get_input_locations(filepath: Path) -> tuple[list[int], list[int]]:
    locations_1 = []
    locations_2 = []
    with open(filepath) as f:
        for line in f:
            words = line.rstrip().split()
            locations_1.append(int(words[0]))
            locations_2.append(int(words[1]))
    return locations_1, locations_2


def get_number_frequency(numbers: list[int]) -> dict[int, int]:
    result = {}
    for number in numbers:
        if number not in result:
            result[number] = 0
        result[number] += 1
    return result


def calc_similarity_score(locations_1: list[int], locations_2: list[int]):
    frequency = get_number_frequency(locations_2)
    score = 0
    for number in locations_1:
        freq = frequency.get(number)
        if freq:
            score += number * freq
    return score


def test_calc_distance():
    locations_1 = [3, 4, 2, 1, 3, 3]
    locations_2 = [4, 3, 5, 3, 9, 3]
    assert calc_distance(locations_1, locations_2) == 11


def test_get_number_frequency():
    numbers = [3, 4, 4, 1, 3, 3]
    assert get_number_frequency(numbers) == {3: 3, 4: 2, 1: 1}


if __name__ == "__main__":
    filepath = Path(__file__).parent.resolve() / "inputs/input_day_1.txt"
    locations_1, locations_2 = get_input_locations(filepath)
    result_part_1 = calc_distance(locations_1, locations_2)
    print(result_part_1)
    result_part_2 = calc_similarity_score(locations_1, locations_2)
    print(result_part_2)

