# Grid index (row, col) increments to move up, down, left, right, up-left,
# up-right, down-left, down-right.
DELTAS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1),
]


def part1(grid: list[str]) -> int:
    target = "XMAS"
    res = 0

    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != "X":
                continue

            for di, dj in DELTAS:
                length = 1
                new_i = i
                new_j = j
                while length < len(target):
                    new_i += di
                    new_j += dj
                    if (
                        new_i < 0
                        or new_i > rows - 1
                        or new_j < 0
                        or new_j > cols - 1
                    ):
                        break
                    elif grid[new_i][new_j] == target[length]:
                        length += 1
                    else:
                        break

                if length == len(target):
                    res += 1

    return res


DIAGONAL_CORNER_PAIRS = [[(-1, -1), (1, 1)], [(-1, 1), (1, -1)]]


def part2(grid: list[str]) -> int:
    res = 0

    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != "A":
                continue

            valid = True
            for corner_pair in DIAGONAL_CORNER_PAIRS:
                corner_chars: set[str] = set()
                for di, dj in corner_pair:
                    new_i = i + di
                    new_j = j + dj
                    if (
                        new_i < 0
                        or new_i > rows - 1
                        or new_j < 0
                        or new_j > cols - 1
                    ):
                        valid = False
                        break

                    corner_chars.add(grid[new_i][new_j])

                if corner_chars != {"M", "S"}:
                    valid = False
                    break

            if valid:
                res += 1

    return res


if __name__ == "__main__":
    with open("data/day4.txt") as f:
        grid = [l.strip() for l in f.readlines()]

    print(part1(grid))
    print(part2(grid))
