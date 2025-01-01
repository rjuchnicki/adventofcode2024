from collections import defaultdict
from functools import cmp_to_key

EXAMPLE_DATA: str = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def parse_input_part1(data: str) -> tuple[defaultdict[list], list[list[str]]]:
    split_input = data.split("\n\n")

    dependencies = split_input[0].strip().split("\n")
    dependency_map = defaultdict(list)
    for dep in dependencies:
        before, after = dep.split("|")
        dependency_map[before].append(after)

    updates = [s.split(",") for s in split_input[1].strip().split("\n")]

    return dependency_map, updates


def parse_input_part2(
    data: str,
) -> tuple[set[tuple[str, str]], list[list[str]]]:
    split_input = data.split("\n\n")

    dependencies = split_input[0].strip().split("\n")
    dependency_set = set()
    for dep in dependencies:
        before, after = dep.split("|")
        dependency_set.add((before, after))

    updates = [s.split(",") for s in split_input[1].strip().split("\n")]

    return dependency_set, updates


def is_valid(update: list[str], dependencies: defaultdict[list]) -> bool:
    valid = True
    pages_produced = set()
    for page in update:
        if not valid:
            break

        for child in dependencies[page]:
            if child in pages_produced:
                valid = False
                break

        pages_produced.add(page)

    return valid


def part1(dependencies: defaultdict[set], updates: list[list[str]]) -> int:
    res = 0
    for update in updates:
        if is_valid(update, dependencies):
            mid = int(len(update) / 2)
            res += int(update[mid])

    return res


def part2(dependencies: set[tuple[str, str]], updates: list[list[str]]) -> int:
    res = 0
    for update in updates:
        sort = sorted(
            update,
            key=cmp_to_key(
                lambda a, b: (
                    -1
                    if (a, b) in dependencies
                    else 1 if (b, a) in dependencies else 0
                )
            ),
        )

        if update != sort:
            print(update, sort)
            mid = int(len(sort) / 2)
            res += int(sort[mid])

    return res


if __name__ == "__main__":
    print(part1(*parse_input_part1(EXAMPLE_DATA)))
    print(part2(*parse_input_part2(EXAMPLE_DATA)))

    with open("data/day5.txt") as f:
        data = f.read()

    print(part1(*parse_input_part1(data)))
    print(part2(*parse_input_part2(data)))
