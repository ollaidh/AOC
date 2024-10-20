from pathlib import Path
from dataclasses import dataclass


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
        move = Move(int(elements[1]), int(elements[3]), int(elements[5]))
        moves.append(move)
    return moves


def move_stacks(stacks: list[list[str]], moves: list[Move]):
    for move in moves:
        counter = 0
        while counter <= move.amount:
            stacks[move.move_from]


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
        Move(1, 2, 1),
        Move(3, 1, 3),
        Move(2, 25, 1),
        Move(1, 1, 2)
    ]
    plan = get_moves_plan(data)
    assert plan == expected_result


def test_move_objects_equal():
    move1 = Move(1, 2, 1)
    move2 = Move(1, 2, 1)
    move3 = Move(2, 2, 1)

    assert move1 == move2
    assert move1 != move3



