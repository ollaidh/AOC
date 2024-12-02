from pathlib import Path


def get_direction(a: int, b: int):
    if b > a:
        return "asc"
    elif b < a:
        return "desc"
    else:
        return "even"


def check_safety(levels: list[str]) -> bool:    
    direction = get_direction(int(levels[0]), int(levels[1]))
    for i in range(len(levels) - 1):
        a = int(levels[i])
        b = int(levels[i + 1])
        if direction != get_direction(a, b) or abs(a - b) == 0 or abs(a - b) > 3:
            return False
    return True


def count_safe_reports(reports: list[list[str]]) -> int:
    safe_counter = 0
    for report in reports:
        if check_safety(report):
            safe_counter += 1
    return safe_counter


def get_input(filepath: Path) -> list[list[str]]:
    reports = []
    with open(filepath) as f:
        for line in f:
            curr_report = line.rstrip().split()
            reports.append(curr_report)
    return reports



def test_check_safety():
    report1 = [7, 6, 4, 2, 1]
    assert check_safety(report1) is True

    report2 = [1, 2, 7, 8, 9]
    assert check_safety(report2) is False

    report3 = [9, 7, 6, 2, 1]
    assert check_safety(report3) is False

    report4 = [1, 3, 2, 4, 5]
    assert check_safety(report4) is False

    report5 = [8, 6, 4, 4, 1]
    assert check_safety(report5) is False

    report6 = [1, 3, 6, 7, 9]
    assert check_safety(report6) is True


if __name__ == "__main__":
    filepath = Path(__file__).parent.resolve() / "inputs/input_day_2.txt"
    reports = get_input(filepath)
    result_part_1 = count_safe_reports(reports)
    print(result_part_1)



