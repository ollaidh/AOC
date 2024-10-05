import pathlib


def load_rucksacks(filepath: str) -> list[tuple[set, set]]:
    rucksacks = []
    with open(filepath) as f:
            lines = f.readlines()
            for line in lines:
                 line.rstrip()
                 line_length = len(line)
                 first_compartment = {line[i] for i in range(0, line_length // 2 )}
                 second_compartment = {line[i] for i in range(line_length // 2, line_length)}
                 rucksacks.append((first_compartment, second_compartment))
    return rucksacks


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
    print(ord("a"))
    filepath = file = pathlib.Path(__file__).parent.resolve() / "inputs/input_day_3.txt"
    rucksacks = load_rucksacks(str(filepath))
    repeated_items_weight = 0
    for rucksack in rucksacks:
        item = find_repeating_item(rucksack)
        if item:
            repeated_items_weight += get_item_weight(item)
    print(repeated_items_weight)