from __future__ import annotations

from pathlib import Path
from dataclasses import dataclass
from typing import Self


@dataclass
class File:
    name: str
    size: int


@dataclass
class Folder:
    name: str
    parent: Self | None
    files: list[File]
    folders: list[Self]


def go(lines: list[str]) -> Folder:
    root_folder = Folder("/", None, [], [])
    curr_folder = root_folder
    for line in lines:
        words = line.split()
        if words[0] == "$":
            if words[1] == "cd":
                if words[2] == "..":
                    curr_folder = curr_folder.parent
                else:
                    curr_folder = Folder(words[2], curr_folder, [], [])
        elif words[1] == "ls":
            pass
        elif words[0] == "dir":
            curr_folder.folders.append(Folder(words[1], curr_folder, [], []))
        else:
            curr_folder.files.append(File(words[1], int(words[0])))
    return root_folder


def test_go():
    lines = [
            "$ cd /",
            "$ ls",
            "dir a",
            "14848514 b.txt",
            "8504156 c.dat",
            "dir d",
            "$ cd a",
            "$ ls",
            "dir e",
            "29116 f",
            "2557 g",
            "62596 h.lst",
            "$ cd e",
            "$ ls",
            "584 i",
            "$ cd ..",
            "$ cd ..",
            "$ cd d",
            "$ ls",
            "4060174 j",
            "8033020 d.log",
            "5626152 d.ext",
            "7214296 k",
    ]

    root = go(lines)
    assert root.name == "/"
    assert root.parent is None
    assert len(root.files) == 2
    assert len(root.folders) == 2
    assert root.files[0].name == "b.txt"
    assert root.files[0].size == 14848514
    assert root.files[0].name == "b.txt"
    assert root.files[0].size == 14848514
    assert root.folders[0].name == "a"
    assert root.folders[0].parent is root
    assert root.folders[1].name == "d"
    assert root.folders[1].parent is root

# - / (dir)
#   - a (dir)
#     - e (dir)
#       - i (file, size=584)
#     - f (file, size=29116)
#     - g (file, size=2557)
#     - h.lst (file, size=62596)
#   - b.txt (file, size=14848514)
#   - c.dat (file, size=8504156)
#   - d (dir)
#     - j (file, size=4060174)
#     - d.log (file, size=8033020)
#     - d.ext (file, size=5626152)
#     - k (file, size=7214296)


if __name__ == "__main__":
    test_go()

