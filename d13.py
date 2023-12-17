import time


def get_patterns(data: list[str]):
    patterns = []
    current_pattern = []
    for line in data:
        if line != "":
            current_pattern.append(line)
        else:
            patterns.append(current_pattern.copy())
            current_pattern = []
    patterns.append(current_pattern.copy())
    return patterns


def compare_lines(line1: str, line2: str) -> bool:
    # print(f"comparin {line1=} and {line2=}")
    if line1 == line2:
        return True
    return False


def count_differences(line1: str, line2: str) -> int:
    assert len(line1) == len(line2)
    count = 0
    for c1, c2 in zip(line1, line2):
        if c1 != c2:
            count += 1
    return count


def find_horizontal_line(pattern: list[str]) -> int:
    found_line = -1
    for i in range(len(pattern) - 1):
        j = 0
        while (i - j) >= 0 and (i + 1 + j) < len(pattern):
            if compare_lines(pattern[i - j], pattern[i + 1 + j]):
                found_line = i
            else:
                found_line = -1
                break
            j += 1
        if found_line >= 0:
            return found_line + 1

    return found_line


def find_horizontal_line_part2(pattern: list[str], old_find: int = -1) -> int:
    old_find = old_find - 1  # because we added one on returning this value before
    found_line = -1
    smudge_found = False
    for i in range(len(pattern) - 1):
        j = 0
        while (i - j) >= 0 and (i + 1 + j) < len(pattern):
            if smudge_found:
                if compare_lines(pattern[i - j], pattern[i + 1 + j]):
                    found_line = i
                else:
                    found_line = -1
                    smudge_found = False
                    break
            else:
                if (
                    compare_lines(pattern[i - j], pattern[i + 1 + j])
                    or count_differences(pattern[i - j], pattern[i + 1 + j]) == 1
                ):
                    found_line = i
                    if count_differences(pattern[i - j], pattern[i + 1 + j]) == 1:
                        # print(i, j)
                        # print(pattern[i - j])
                        # print(pattern[i + 1 + j])
                        # print(found_line)
                        smudge_found = True
                else:
                    found_line = -1
                    smudge_found = False
                    break
            j += 1
        if found_line >= 0 and smudge_found and found_line != old_find:
            return found_line + 1

    return -1


def find_vertical_line(pattern: list[str]) -> int:
    width = len(pattern[0])
    found_line = -1

    for i in range(width - 1):
        j = 0
        while (i - j) >= 0 and (i + 1 + j) < width:
            col_1 = "".join([line[i - j] for line in pattern])
            col_2 = "".join([line[i + 1 + j] for line in pattern])
            if compare_lines(col_1, col_2):
                found_line = i
            else:
                found_line = -1
                break
            j += 1
        if found_line >= 0:
            return found_line + 1

    return found_line


def find_vertical_line_part2(pattern: list[str], old_find=-1) -> int:
    old_find = old_find - 1  # because we added one on returning this value before
    width = len(pattern[0])
    found_line = -1
    smudge_found = False
    for i in range(width - 1):
        j = 0
        while (i - j) >= 0 and (i + 1 + j) < width:
            col_1 = "".join([line[i - j] for line in pattern])
            col_2 = "".join([line[i + 1 + j] for line in pattern])
            if smudge_found:
                if compare_lines(col_1, col_2):
                    found_line = i
                else:
                    found_line = -1
                    smudge_found = False

            else:
                if compare_lines(col_1, col_2) or count_differences(col_1, col_2) == 1:
                    found_line = i
                    if count_differences(col_1, col_2) == 1:
                        smudge_found = True
                else:
                    found_line = -1
                    smudge_found = False
                    break
            j += 1
        if found_line >= 0 and smudge_found and found_line != old_find:
            return found_line + 1

    return -1


def solve_part1(data: list[str]):
    patterns = get_patterns(data)
    total = 0
    vert = 0
    hor = 0
    # looking for horizontal lines
    for i, pattern in enumerate(patterns):
        print(f"Pattern Nr {i}")
        hor = find_horizontal_line(pattern)
        print(f"{hor=}")
        total += 100 * max(hor, 0)
        if hor == -1:
            vert = find_vertical_line(pattern)
            print(f"{vert=}")
            total += vert
        if hor == 0 and vert == 0:
            for line in pattern:
                print(line)
    return total


def solve_part2(data: list[str]):
    patterns = get_patterns(data)
    total = 0
    vert = 0
    hor = 0
    # looking for horizontal lines
    for i, pattern in enumerate(patterns):
        vert = 0
        hor = 0
        print(f"Pattern Nr {i}")
        hor_old = find_horizontal_line(pattern)
        hor = find_horizontal_line_part2(pattern, hor_old)
        # print(f"{hor_old=}")
        # print(f"{hor=}")
        total += 100 * max(hor, 0)
        if hor == -1:
            vert_old = find_vertical_line(pattern)
            vert = find_vertical_line_part2(pattern, vert_old)
            # print(f"{vert_old=}")
            # print(f"{vert=}")
            total += vert
        if hor == 0 and vert == 0:
            for line in pattern:
                print(line)
        subtotal = max(vert, 0) + max(hor, 0) * 100
        # print(f"{vert=}")
        print(f"{subtotal=}")
    return total


def solve_part2_rev(data: list[str]):
    patterns = get_patterns(data)
    total = 0
    vert = 0
    hor = 0
    # looking for horizontal lines
    for i, pattern in enumerate(patterns):
        vert = 0
        hor = 0
        print(f"Pattern Nr {i}")
        vert_old = find_vertical_line(pattern)
        vert = find_vertical_line_part2(pattern, vert_old)
        # print(f"{vert_old=}")
        # print(f"{vert=}")
        total += max(vert, 0)
        if vert == -1:
            hor_old = find_horizontal_line(pattern)
            hor = find_horizontal_line_part2(pattern, hor_old)
            # print(f"{hor_old=}")
            # print(f"{hor=}")
            total += hor * 100
        if hor == 0 and vert == 0:
            for line in pattern:
                print(line)
        subtotal = max(vert, 0) + max(hor, 0) * 100
        # print(f"{vert=}")
        print(f"{subtotal=}")
    return total


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():
    day = 13

    data = read_data(f"d{day}_input.txt")
    # data = read_data(f"d{day}_sample.txt")
    # data = read_data(f"d{day}_sampleb.txt")

    start_time = time.perf_counter_ns()
    print(f"Solution Day {day}, Part1:")
    print(solve_part1(data))
    print(f"Time for part 1: {(time.perf_counter_ns()-start_time)/1000} µs")

    start_time = time.perf_counter_ns()
    print(f"Solution Day {day}, Part2:")

    print(solve_part2(data))

    print(solve_part2_rev(data))
    print(f"Time for part 2: {(time.perf_counter_ns()-start_time)/1000} µs")


if __name__ == "__main__":
    main()
