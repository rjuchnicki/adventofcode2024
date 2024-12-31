import re

def part1(data: str) -> int:
    res = 0
    for m in re.finditer(r"mul\((\d+),(\d+)\)", data):
        res += (int(m[1]) * int(m[2]))

    return res


def part2(data: str) -> int:
    res = 0
    enabled = True
    for m in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", data):
        if m[0] == "do()":
            enabled = True
        elif m[0] == "don't()":
            enabled = False
        elif enabled:
            res += (int(m[1]) * int(m[2]))

    return res


if __name__ == "__main__":
    with open("data/day3.txt") as f:
        data = f.read()

    print(part1(data))
    print(part2(data))
