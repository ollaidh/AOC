from __future__ import annotations

from pathlib import Path
from dataclasses import dataclass


@dataclass
class File:
    name: str
    size: int


@dataclass
class Folder:
    name: str
    parent: Folder
    files: list[File]
    folders: list[Folder]


if __name__ == '__main__':
    pass



