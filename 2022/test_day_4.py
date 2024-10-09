import pathlib

def read_pairs(filepath: pathlib.Path) -> list[list[list[int]]]:
    pairs = []
    with open(filepath) as f:
          lines = f.readlines()

    for line in lines:
        line = line.rstrip()
        first_elf = [int(x) for x in line.split(",")[0].split("-")]
        second_elf = [int(x) for x in line.split(",")[1].split("-")]

        pairs.append([first_elf, second_elf])

    return pairs

def count_full_overlaps(pairs: list[list[list[int]]]) -> int:
    counter = 0
    for pair in pairs:
        if (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]) or (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]):
                counter += 1
    return counter
          


if __name__ == "__main__":
        filepath = pathlib.Path(__file__).parent.resolve() / "inputs/input_day_4.txt"
        pairs = read_pairs(filepath)
        print(count_full_overlaps(pairs))
