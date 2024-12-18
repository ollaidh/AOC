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
    size: int = 0

    def get_child_folder(self, name: str) -> Self | None:
        for folder in self.folders:
            if folder.name == name:
                return folder
        return None
    
    def compute_folder_size(self) -> int:
        for file in self.files:
            self.size += file.size
        for folder in self.folders:
            self.size += folder.compute_folder_size()
        return self.size
    

def get_sum_size_folders_less_cutoff(root: Folder, cutoff: int) -> int:
    result = 0
    def calc(root: Folder):
        if root.size <= cutoff:
            nonlocal result
            result += root.size
        for folder in root.folders:
            calc(folder)
    calc(root)
    return result


def calc_additional_space_needed(disk_size: int, size_to_run: int, root_size: int) -> int:
    result = max(size_to_run - (disk_size - root_size), 0)
    return result


def calc_folder_to_delete_size(root: Folder, min_folder_size: int) -> int:
    if min_folder_size == 0:
        return 0
    result = root.size
    def calc(root: Folder):
        if root.size >= min_folder_size:
            nonlocal result
            result = min(result, root.size)
        for folder in root.folders:
            calc(folder)
    calc(root)
    return result


def parse_folder_from_lines(lines: list[str]) -> Folder:
    root_folder = Folder("/", None, [], [])
    curr_folder: Folder | None = root_folder
    for line in lines[1:]:
        assert curr_folder is not None
        words = line.split()
        if words[0] == "$":
            if words[1] == "cd":
                if words[2] == "..":                    
                    curr_folder = curr_folder.parent
                else:
                    curr_folder = curr_folder.get_child_folder(words[2])
                    assert curr_folder is not None
        elif words[1] == "ls":
            pass
        elif words[0] == "dir":
            curr_folder.folders.append(Folder(words[1], curr_folder, [], []))
        else:
            curr_folder.files.append(File(words[1], int(words[0])))
    root_folder.compute_folder_size()
    return root_folder


def read_input_from_file(filepath: Path) -> list[str]:
    with open(filepath) as f:
        result = f.readlines()
    return result



def test_folder_get_child_folder():
    root = Folder("aaa", None, [], [])
    
    child1 = Folder("bbb_1", None, [], [])  # parents are skipped here
    root.folders.append(child1)
    
    child2 = Folder("bbb_2", None, [], [])
    root.folders.append(child2)

    assert root.get_child_folder("bbb_1") is child1
    assert root.get_child_folder("bbb_2") is child2
    assert root.get_child_folder("zzz") is None


def test_parse_folder_from_lines():
    """
    Parsing input to get the following folder structure:
        - / (dir)
            - a (dir)
                - e (dir)
                    - i (file, size=584)
                - f (file, size=29116)
                - g (file, size=2557)
                - h.lst (file, size=62596)
            - b.txt (file, size=14848514)
            - c.dat (file, size=8504156)
            - d (dir)
                - j (file, size=4060174)
                - d.log (file, size=8033020)
                - d.ext (file, size=5626152)
                - k (file, size=7214296)
    """

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

    root = parse_folder_from_lines(lines)
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

    assert len(root.folders[0].folders) == 1
    assert len(root.folders[0].files) == 3
    assert root.folders[0].folders[0].name == "e"
    assert root.folders[0].files[0].name == "f"
    assert root.folders[0].files[0].size == 29116
    assert root.folders[0].files[1].name == "g"
    assert root.folders[0].files[1].size == 2557
    assert root.folders[0].files[2].name == "h.lst"
    assert root.folders[0].files[2].size == 62596

    assert len(root.folders[0].folders[0].folders) == 0
    assert len(root.folders[0].folders[0].files) == 1
    assert root.folders[0].folders[0].files[0].name == "i"
    assert root.folders[0].folders[0].files[0].size == 584


def test_compute_folder_sum_size():
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

    # test size of each folder:
    root = parse_folder_from_lines(lines)
    assert root.folders[0].folders[0].size == 584  # e dir
    assert root.folders[0].size == 94853  # a dir
    assert root.folders[1].size == 24933642  # d dir
    assert root.size == 48381165  # / dir

    # test total size of folders with size less than cutoff:
    result = get_sum_size_folders_less_cutoff(root, 100000)
    assert result == 95437

    additional_space = calc_additional_space_needed(70000000, 30000000, root.size)
    assert additional_space == 8381165

    folder_size_to_delete = calc_folder_to_delete_size(root, additional_space)
    assert folder_size_to_delete == 24933642


if __name__ == "__main__":
    filepath = Path(__file__).parent.resolve() / "inputs/input_day_7.txt"
    lines = read_input_from_file(filepath)
    root = parse_folder_from_lines(lines)
    result_part_1 = get_sum_size_folders_less_cutoff(root, 100000)
    print(result_part_1)