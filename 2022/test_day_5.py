from pathlib import Path
from dataclasses import dataclass
from typing import Callable


@dataclass
class Move:
    amount: int
    move_from: int
    move_to: int


def get_stacks_plan(lines: list[str]) -> list[list[str]]:
    stacks = []
    for i in range(len(lines[0])):
        if lines[-1][i] == " ":
            continue

        curr_stack = []
        for j in range(len(lines) - 2, -1, -1):
            if lines[j][i] != " " :
                curr_stack.append(lines[j][i])
        stacks.append(curr_stack)

    return stacks


def get_moves_plan(lines: list[str]) -> list[Move]:
    moves = []
    for line in lines:
        elements = line.split()
        move = Move(int(elements[1]), int(elements[3]) - 1, int(elements[5]) - 1)
        moves.append(move)
    return moves


def move_stacks_one_by_one(stacks: list[list[str]], moves: list[Move]) -> list[list[str]]:
    for move in moves:
        counter = 0
        while counter < move.amount:
            print(counter)
            stacks[move.move_to].append(stacks[move.move_from][-1])
            stacks[move.move_from].pop()
            counter += 1
    return stacks


def move_stacks_by_packs(stacks: list[list[str]], moves: list[Move]) -> list[list[str]]:
    for move in moves:
        n = len(stacks[move.move_from]) - move.amount
        stacks[move.move_to].extend(stacks[move.move_from][n:])
        stacks[move.move_from] = stacks[move.move_from][:n]
    return stacks


def get_stacks_top_layer(stacks: list[list[str]]) -> str:
    tops = []
    for stack in stacks:
        if stack:
            tops.append(stack[-1])
        else:
            tops.append(" ")

    return ''.join(tops)


def action(stacks: list[str], moves: list[str], move_func: Callable) -> str:
    parsed_stacks = get_stacks_plan(stacks)
    parsed_moves = get_moves_plan(moves)
    rearranged_stacks = move_func(parsed_stacks, parsed_moves)
    result = get_stacks_top_layer(rearranged_stacks)
    return result


def read_stacks_moves_from_file(filepath: Path) -> tuple:
    mode = "stacks"
    stacks = []
    moves = []
    with open(filepath) as f:
        for line in f:
            if line != "\n":
                if mode == "stacks":
                    stacks.append(line)
                else:
                    moves.append(line)
            else:
                mode = "moves"
    return stacks, moves


def test_get_stacks():
    data = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
    ]
    expected = [
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"]
    ]
    stacks = get_stacks_plan(data)
    assert stacks == expected

    data = [
        "    [D]        ",
        "[N] [C]        ",
        "[Z] [M] [P]    ",
        " 1   2   3   4 ",
    ]
    expected = [
        ["Z", "N"],
        ["M", "C", "D"],
        ["P"],
        []
    ]
    stacks = get_stacks_plan(data)
    assert stacks == expected


def test_get_plan():
    data = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 25 to 1",
        "move 1 from 1 to 2"
    ]
    expected_result = [
        Move(1, 1, 0),
        Move(3, 0, 2),
        Move(2, 24, 0),
        Move(1, 0, 1)
    ]
    plan = get_moves_plan(data)
    assert plan == expected_result


def test_move_objects_equal():
    move1 = Move(1, 2, 1)
    move2 = Move(1, 2, 1)
    move3 = Move(2, 2, 1)

    assert move1 == move2
    assert move1 != move3


def test_move_stacks_one_by_one():
    stacks_input = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
    ]

    stacks = get_stacks_plan(stacks_input)

    moves_input = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2"
    ]

    moves = get_moves_plan(moves_input)

    expected_result = "CMZ"

    result = get_stacks_top_layer(move_stacks_one_by_one(stacks, moves))

    assert expected_result == result


def test_move_stacks_by_pack():
    stacks_input = [
        "    [D]    ",
        "[N] [C]    ",
        "[Z] [M] [P]",
        " 1   2   3 ",
    ]

    stacks = get_stacks_plan(stacks_input)

    moves_input = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2"
    ]

    moves = get_moves_plan(moves_input)

    expected_result = "MCD"

    result = get_stacks_top_layer(move_stacks_by_packs(stacks, moves))

    assert expected_result == result


if __name__ == "__main__":
    filepath = filepath = Path(__file__).parent.resolve() / "inputs/input_day_5.txt"
    stacks, moves = read_stacks_moves_from_file(filepath)
    result_part_1 = action(stacks, moves, move_stacks_one_by_one)
    result_part_2 = action(stacks, moves, move_stacks_by_packs)
    print(result_part_1)
    print(result_part_2)