import pathlib

figures_weights = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

figures_relations = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}

required_results = {"X": 0, "Y": 3, "Z": 6}


def get_data_from_file(filepath: str) -> list[list[str]]:
    file = pathlib.Path(__file__).parent.resolve() / filepath
    moves = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            move = line.rstrip().split()
            moves.append(move)
    return moves


def define_my_moves(plan: list[list[str]]):
    for i in range(len(plan)):
        elf_move = plan[i][0]
        required_result = plan[i][1]
        for key, value in figures_relations[elf_move].items():
            if value == required_results[required_result]:
                plan[i][1] = key
    return plan


def play_round(my_move: str, elf_move: str) -> int:
    return figures_relations[elf_move][my_move] + figures_weights[my_move]


def play(moves: list[list[str]]) -> int:
    result = 0
    for move in moves:
        result += play_round(move[1], move[0])
    return result


def test_play():
    moves = [
        ["A", "Y"],
        ["B", "X"],
        ["C", "Z"],
    ]

    assert play(moves) == 15


if __name__ == "__main__":
    data = get_data_from_file("inputs/input_day_2.txt")
    first_part_result = play(data)
    moves = define_my_moves(data)
    second_part_result = play(moves)
    print(second_part_result)
