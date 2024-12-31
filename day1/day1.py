from collections import Counter

def part1(left: list[int], right: list[int]):
    left.sort()
    right.sort()

    total = 0
    for i in range(len(left)):
        total += abs(left[i] - right[i])
    
    return total


def part2(left: list[int], right: list[int]):
    counts = Counter(right)

    total = 0
    for num in left:
        if num in counts:
            total += (num * counts[num])
    
    return total


if __name__ == "__main__":
    with open("data/day1.txt") as f:
        data = [l.split() for l in f.readlines()]
    left = [int(d[0]) for d in data]
    right = [int(d[1]) for d in data]
    
    print(part1(left, right))
    print(part2(left, right))
