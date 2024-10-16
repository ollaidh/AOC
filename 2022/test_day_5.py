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
        curr_stack = []
        for j in range(len(lines) - 2, -1, -1):
            if lines[len(lines) - 1][i] != " " and lines[j][i] != " " :
                curr_stack.append(lines[j][i])
        if curr_stack:
            stacks.append(curr_stack)
    return stacks


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
    print(expected)
    print(stacks)
    assert stacks == expected


