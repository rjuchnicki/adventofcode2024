import itertools
from typing import LiteralString


def solve(
    equations: list[str] | list[LiteralString],
    operators: list[str] = ["*", "+"],
) -> int:
    total = 0

    for equation in equations:
        test_value, operands = equation.split(":")
        test_value = int(test_value)
        operands = [int(op) for op in operands.split()]

        for operator_sequence in itertools.product(
            operators, repeat=len(operands) - 1
        ):
            res = operands[0]
            for i in range(len(operator_sequence)):
                op = operator_sequence[i]
                if op == "*":
                    res *= operands[i + 1]
                elif op == "+":
                    res += operands[i + 1]
                elif op == "||":
                    res = int(str(res) + str(operands[i + 1]))

            if res == test_value:
                total += res
                break

    return total


EXAMPLE_INPUT = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


if __name__ == "__main__":
    part_2_ops = ["*", "+", "||"]
    print(solve(EXAMPLE_INPUT.strip().split("\n")))
    print(solve(EXAMPLE_INPUT.strip().split("\n"), part_2_ops))

    with open("data/day7.txt") as f:
        equations = f.readlines()

    print(solve(equations))
    print(solve(equations, part_2_ops))
