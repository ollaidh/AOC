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

def count_overlaps(pairs: list[list[list[int]]]) -> int:
    counter = 0
    for pair in pairs:
        begin_1 = pair[0][0]
        end_1 = pair[0][1]
        begin_2 = pair[1][0]
        end_2 = pair[1][1]

        if  begin_1 <= begin_2 <= end_1 or begin_2 <= begin_1 <= end_2:
             counter += 1

    return counter

# (3, 8) (1, 4)
          

if __name__ == "__main__":
        filepath = pathlib.Path(__file__).parent.resolve() / "inputs/input_day_4.txt"
        pairs = read_pairs(filepath)
        result_part_1 = count_full_overlaps(pairs)
        result_part_2 = count_overlaps(pairs)
