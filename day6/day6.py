UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

ROTATIONS: dict[tuple[int, int], tuple[int, int]] = {
    UP: RIGHT,
    RIGHT: DOWN,
    DOWN: LEFT,
    LEFT: UP,
}


def in_bounds(i: int, j: int, grid: list[list[str]]) -> bool:
    return 0 <= i <= len(grid) - 1 and 0 <= j <= len(grid[0]) - 1


def part1(grid: list[list[str]], guard_position: tuple[int, int]) -> int:
    direction = UP
    i, j = guard_position
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    while in_bounds(i, j, grid):
        visited[i][j] = True

        di, dj = direction
        next_i = i + di
        next_j = j + dj
        if in_bounds(next_i, next_j, grid) and grid[next_i][next_j] == "#":
            direction = ROTATIONS[direction]
        else:
            i = next_i
            j = next_j

    return sum(sum(row) for row in visited)


def part2(grid: list[list[str]], guard_position: tuple[int, int]) -> int:
    loops = 0

    for k in range(len(grid)):
        for l in range(len(grid[0])):
            if grid[k][l] == "#":
                continue
            grid[k][l] = "#"

            direction = UP
            i, j = guard_position
            visited: set[tuple[int, int, tuple[int, int]]] = set()
            while in_bounds(i, j, grid):
                state: tuple[int, int, tuple[int, int]] = (i, j, direction)
                if state in visited:
                    loops += 1
                    break

                visited.add(state)

                di, dj = direction
                next_i = i + di
                next_j = j + dj
                if (
                    in_bounds(next_i, next_j, grid)
                    and grid[next_i][next_j] == "#"
                ):
                    direction = ROTATIONS[direction]
                else:
                    i = next_i
                    j = next_j

            grid[k][l] = "."

    return loops


def get_guard_position(grid: list[list[str]]) -> tuple[int, int]:
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                return (i, j)

    return (-1, -1)


EXAMPLE_DATA = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


if __name__ == "__main__":
    example_grid = [[c for c in l.strip()] for l in EXAMPLE_DATA.split()]
    print(part1(example_grid, get_guard_position(example_grid)))
    print(part2(example_grid, get_guard_position(example_grid)))

    with open("data/day6.txt") as f:
        grid = [[c for c in l.strip()] for l in f.readlines()]

    print(part1(grid, get_guard_position(grid)))
    print(part2(grid, get_guard_position(grid)))
