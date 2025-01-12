def part1(data: str) -> int:
    disk: list[int] = []
    file = True
    id = 0
    num_file_blocks = 0
    for d in data:
        size = int(d)
        if file:
            disk.extend([id] * size)
            num_file_blocks += size
            id += 1
        else:
            disk.extend([-1] * size)

        file = not file

    last_int = len(disk) - 1
    i = 0
    res = 0
    while i < num_file_blocks:
        while disk[last_int] == -1:
            last_int -= 1

        if disk[i] == -1:
            res += i * disk[last_int]
            last_int -= 1
        else:
            res += i * disk[i]

        i += 1

    return res


def part2(data: str) -> int:
    file = True
    id = 0
    pos = 0
    file_to_position_length: dict[int, tuple[int, int]] = {}
    gaps: list[tuple[int, int]] = []
    for d in data:
        size = int(d)
        if file:
            file_to_position_length[id] = (pos, size)
            id += 1
        elif size > 0:
            gaps.append((pos, size))

        pos += size
        file = not file

    id -= 1
    for i in range(id, 0, -1):
        pos, l = file_to_position_length[i]
        for j in range(len(gaps)):
            gap_pos, gap_l = gaps[j]
            if gap_pos > pos:
                break
            elif l > gap_l:
                continue

            file_to_position_length[i] = (gap_pos, l)
            if l < gap_l:
                gaps[j] = (gap_pos + l, gap_l - l)
            else:
                gaps.pop(j)

            break

    res = 0
    for file, (pos, l) in file_to_position_length.items():
        for i in range(l):
            res += (pos + i) * file

    return res


if __name__ == "__main__":
    with open("data/day9.txt") as f:
        data = f.read().strip()

    print(part1("2333133121414131402"))
    print(part1(data))
    print(part2("2333133121414131402"))
    print(part2(data))
