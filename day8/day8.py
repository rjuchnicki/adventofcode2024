from collections import defaultdict
from typing import LiteralString


def part1(grid: list[str] | list[LiteralString]) -> int:
    antinodes: set[tuple[int, int]] = set()
    antennas: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)

    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            antenna_id = grid[i][j]
            if not antenna_id.isalnum():
                continue

            for match_i, match_j in antennas[antenna_id]:
                di = i - match_i
                dj = j - match_j
                for antinode_i, antinode_j, sign in [
                    (i, j, 1),
                    (match_i, match_j, -1),
                ]:
                    antinode_i += sign * di
                    antinode_j += sign * dj
                    if (
                        0 <= antinode_i <= rows - 1
                        and 0 <= antinode_j <= cols - 1
                    ):
                        antinodes.add((antinode_i, antinode_j))

            antennas[antenna_id].append((i, j))

    return len(antinodes)


def part2(grid: list[str] | list[LiteralString]) -> int:
    antinodes: set[tuple[int, int]] = set()
    antennas: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)

    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            antenna_id = grid[i][j]
            if not antenna_id.isalnum():
                continue

            for match_i, match_j in antennas[antenna_id]:
                di = i - match_i
                dj = j - match_j
                for antinode_i, antinode_j, sign in [
                    (i, j, 1),
                    (match_i, match_j, -1),
                ]:
                    antinode_i += sign * di
                    antinode_j += sign * dj
                    while (
                        0 <= antinode_i <= rows - 1
                        and 0 <= antinode_j <= cols - 1
                    ):
                        antinodes.add((antinode_i, antinode_j))
                        antinode_i += sign * di
                        antinode_j += sign * dj

            antinodes.add((i, j))
            antennas[antenna_id].append((i, j))

    return len(antinodes)


EXAMPLE_INPUT = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""


if __name__ == "__main__":
    print(part1(EXAMPLE_INPUT.strip().splitlines()))
    print(part2(EXAMPLE_INPUT.strip().splitlines()))

    with open("data/day8.txt") as f:
        grid = [l.strip() for l in f.readlines()]

    print(part1(grid))
    print(part2(grid))
