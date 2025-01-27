DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def num_trails(
    grid: list[list[int]],
    i: int,
    j: int,
    reached_nines: set[tuple[int, int]],
    count_trails: bool,
) -> int:
    current = grid[i][j]
    if current == 9:
        if not count_trails and (i, j) in reached_nines:
            return 0
        else:
            reached_nines.add((i, j))
            return 1

    valid: list[tuple[int, int]] = []
    for di, dj in DIRS:
        new_i = i + di
        new_j = j + dj
        if (
            0 <= new_i < len(grid)
            and 0 <= new_j < len(grid[0])
            and grid[new_i][new_j] == current + 1
        ):
            valid.append((new_i, new_j))

    if len(valid) == 0:
        return 0

    return sum(
        num_trails(grid, x, y, reached_nines, count_trails) for x, y in valid
    )


def solve(grid: list[list[int]], count_trails: bool = True) -> int:
    ret = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                reached_nines: set[tuple[int, int]] = set()
                ret += num_trails(
                    grid, i, j, reached_nines, count_trails=count_trails
                )

    return ret


# Part 1 expected answer: 1
# Part 2 expected answer: 2
SMALL_EXAMPLE = """0123
1234
8765
9876"""

# Part 1 expected answer: 36
# Part 2 expected answer: 81
EXAMPLE = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

if __name__ == "__main__":
    with open("data/day10.txt") as f:
        grid = [[int(i) for i in l.strip()] for l in f.readlines()]

    example_grid = [[int(i) for i in l.strip()] for l in EXAMPLE.split("\n")]
    print(solve(example_grid, count_trails=False))
    print(solve(grid, count_trails=False))

    print(solve(example_grid))
    print(solve(grid))
