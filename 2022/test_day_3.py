import pathlib


def load_rucksacks(filepath: str) -> list:
    with open(filepath) as f:
            lines = f.readlines()
    return lines 


def split_items_into_compartments(rucksack: str) -> tuple[set, set]:
    rucksack.rstrip()
    line_length = len(rucksack)
    first_compartment = {rucksack[i] for i in range(0, line_length // 2 )}
    second_compartment = {rucksack[i] for i in range(line_length // 2, line_length)}
    return first_compartment, second_compartment


def find_repeating_item(rucksack: tuple[set, set]) -> str | None:
    for item in rucksack[0]:
        if item in rucksack[1]:
            return item
    return None


def get_item_weight(item: str):
    if ord(item) < 91:     
        return ord(item) - ord("A") + 27
    else:
        return ord(item) - ord("a") + 1
     

if __name__ == "__main__":
    filepath = file = pathlib.Path(__file__).parent.resolve() / "inputs/input_day_3.txt"
    rucksacks = load_rucksacks(str(filepath))
    part_1_result = 0
    for rucksack in rucksacks:
        rucksack = split_items_into_compartments(rucksack)
        item = find_repeating_item(rucksack)
        if item:
            part_1_result += get_item_weight(item)
    print(part_1_result)

