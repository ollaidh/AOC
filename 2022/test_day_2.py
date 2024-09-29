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


def play_round(my_move: int, elf_move: int) -> int:
    return figures_relations[elf_move][my_move] + figures_weights[my_move]


def play(moves: list[list[str]]) -> int:
    result = 0
    for move in moves:
        result  += play_round(move[1], move[0])
    return result


def get_moves_from_file(filepath: str) -> list[list[str]]:
    file = pathlib.Path(__file__).parent.resolve() / filepath
    moves = []
    with open(file) as f:
        lines = f.readlines()
        for line in lines:
            move = line.rstrip().split()
            moves.append(move)
    return moves


def test_play():
    moves = [
        ["A", "Y"],
        ["B", "X"],
        ["C", "Z"],
    ]

    assert play(moves) == 15


if __name__ == "__main__":
   moves = get_moves_from_file("inputs/input_day_2.txt")
   print(play(moves))

