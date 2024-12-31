def is_safe(report: list[int]) -> int:
    for i in range(len(report) - 1):
        a = report[i]
        b = report[i + 1]
        delta = a - b
        if delta < 1 or delta > 3:
            return False
    
    return True


def part1(reports: list[list[int]]) -> int:     
    return sum(is_safe(report) or is_safe(report[::-1]) for report in reports)


def is_safe_with_dampening(report: list[int]) -> int:
    for i in range(len(report) - 1):
        a = report[i]
        b = report[i + 1]
        delta = a - b
        if delta < 1 or delta > 3:
            return any(is_safe(report[j - 1 : j] + report[j + 1:]) for j in [i, i + 1])
    
    return True


def part2(reports: list[list[int]]) -> int:
    return sum(is_safe_with_dampening(report) or is_safe_with_dampening(report[::-1]) for report in reports)


if __name__ == "__main__":
    with open("data/day2.txt") as f:
        reports = [list(map(int, l.split())) for l in f.readlines()]

    print(part1(reports))
    print(part2(reports))
