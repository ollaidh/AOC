from pathlib import Path


def find_marker(input_data: str, packet_length: int) -> int:
    data = list(input_data)
    curr_pack = dict()
    for i in range (packet_length):
        curr_pack[data[i]] = curr_pack.get(data[i], 0)
        curr_pack[data[i]] = curr_pack[data[i]] + 1
    if len(curr_pack) == packet_length:
        return packet_length
    i = packet_length
    while i < len(data) - 1:
        if curr_pack[data[i - packet_length]] == 1:
            curr_pack.pop(data[i - packet_length])
        else:
            curr_pack[data[i - packet_length]] = curr_pack[data[i - packet_length]] - 1
        curr_pack[data[i]] = curr_pack.get(data[i], 0)
        curr_pack[data[i]] = curr_pack[data[i]] + 1
        if len(curr_pack) == packet_length:
            return i + 1
        i += 1
    return -1


def get_signal(filepath: Path) -> str:
    with open(filepath) as f:
        signal = f. read()

    return signal



def test_find_marker():
    data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
    result = find_marker(data, 4)
    assert result == 5

    data = "nppdvjthqldpwncqszvftbrmjlhg"
    result = find_marker(data, 4)
    assert result == 6

    data = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
    result = find_marker(data, 4)
    assert result == 10

    data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    result = find_marker(data, 4)
    assert result == 11


if __name__ == "__main__":
    signal = get_signal(Path(__file__).parent.resolve() / "inputs/input_day_6.txt")
    result_part_1 = find_marker(signal, 4)
    print(result_part_1)
    result_part_2 = find_marker(signal, 14)
    print(result_part_2)

