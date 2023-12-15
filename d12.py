import time
from itertools import permutations, product
import re

search = re.compile(r"#+")


def get_control_number(springs: str) -> list[int]:
    """returns a list of the lengths of consecutive "#"
    eg:

    get_control_number("#.#.###")==[1,1,3]"""
    numbers = []
    current_count = 0
    for c in springs:
        if c == "." and current_count != 0:
            numbers.append(current_count)
            current_count = 0
        elif c == "#":
            current_count += 1
    if current_count > 0:
        numbers.append(current_count)
    return numbers


def get_control_number_regex(springs: str) -> list[int]:
    """returns a list of the length of consecutive "#" """
    numbers = [match.end() - match.start() for match in search.finditer(springs)]
    return numbers


def solve_part1(data: list[str]):
    count_total = 0
    for line in data:
        count_this_line = 0
        springs, control = line.split()
        control = [int(i) for i in control.split(",")]
        n_unknown = springs.count("?")
        n_known = springs.count("#")
        n_damaged = sum(control)
        # print(f"{n_unknown=} {n_known=} {n_damaged=}")
        # get all posible permutations of needed fields
        perms = product(".#", repeat=n_unknown)
        for perm in perms:
            if perm.count("#") + n_known != n_damaged:
                continue
            new_springs = springs
            for c in perm:
                new_springs = new_springs.replace("?", c, 1)
            if get_control_number(new_springs) == control:
                count_this_line += 1
        count_total += count_this_line
    return count_total


def solve_part2(data: list[str]):
    count_total = 0
    for i, line in enumerate(data):
        count_this_line = 0

        springs, control = line.split()
        springs = (springs + "?") * 5
        springs = springs[:-1]  # remove trailing "?" after copying

        control = [int(i) for i in control.split(",")]
        control = control * 5

        n_unknown = springs.count("?")
        n_known = springs.count("#")
        n_damaged = sum(control)
        # print(f"{n_unknown=} {n_known=} {n_damaged=}")
        # get all posible permutations of needed fields
        permutations = product(".#", repeat=n_unknown)

        for perm in permutations:
            if perm.count("#") + n_known != n_damaged:
                continue
            new_springs = springs
            for c in perm:
                new_springs = new_springs.replace("?", c, 1)
            if get_control_number(new_springs) == control:
                count_this_line += 1

        count_total += count_this_line
    return count_total


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def test_count():
    assert get_control_number("#.#.###") == [1, 1, 3]
    assert get_control_number_regex("#.#.###") == [1, 1, 3]


def main():
    day = 12

    data = read_data(f"d{day}_input.txt")
    # data = read_data(f"d{day}_sample.txt")

    start_time = time.perf_counter_ns()
    print(f"Solution Day {day}, Part1:")
    print(solve_part1(data))
    print(f"Time for part 1: {(time.perf_counter_ns()-start_time)/1000} µs")

    start_time = time.perf_counter_ns()
    print(f"Solution Day {day}, Part2:")
    print(solve_part2(data))
    print(f"Time for part 2: {(time.perf_counter_ns()-start_time)/1000} µs")


if __name__ == "__main__":
    test_count()

    main()
