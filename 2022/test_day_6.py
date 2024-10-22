from pathlib import Path


def find_marker(input_data: str) -> int:
    data = list(input_data)
    curr_pack = dict()
    for i in range (4):
        curr_pack[data[i]] = curr_pack.get(data[i], 0)
        curr_pack[data[i]] = curr_pack[data[i]] + 1
    if len(curr_pack) == 4:
        return 4
    i = 4
    while i < len(data) - 1:
        if curr_pack[data[i - 4]] == 1:
            curr_pack.pop(data[i - 4])
        else:
            curr_pack[data[i - 4]] = curr_pack[data[i - 4]] - 1
        curr_pack[data[i]] = curr_pack.get(data[i], 0)
        curr_pack[data[i]] = curr_pack[data[i]] + 1
        if len(curr_pack) == 4:
            return i + 1
        i += 1
    return -1


def get_signal(filepath: Path) -> str:
    with open(filepath) as f:
        signal = f. read()

    return signal



def test_find_marker():
    data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    result = find_marker(data)
    assert result == 5

    data = "nppdvjthqldpwncqszvftbrmjlhg"
    result = find_marker(data)
    assert result == 6

    data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    result = find_marker(data)
    assert result == 10

    data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    result = find_marker(data)
    assert result == 11


if __name__ == "__main__":
    signal = get_signal(Path(__file__).parent.resolve() / "inputs/input_day_6.txt")
    result_part_1 = find_marker(signal)
    print(result_part_1)