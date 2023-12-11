import time
from typing import NewType
from itertools import permutations

Point = NewType("Point", list[int])


def get_stars(data: list[str]) -> list[Point]:
    stars = []
    for row, line in enumerate(data):
        for col, c in enumerate(line):
            if c == "#":
                stars.append([row, col])
    return stars


def get_empt_rows(data: list[str]) -> list[int]:
    empt_rows = []
    for row, line in enumerate(data):
        if all([c == "." for c in line]):
            empt_rows.append(row)
    return empt_rows


def get_empt_col(data: list[str]) -> list[int]:
    empt_col = []
    for i in range(len(data[0])):
        empty = True
        for line in data:
            if line[i] == "#":
                empty = False
        if empty:
            empt_col.append(i)

    return empt_col


def get_distance(p1: Point, p2: Point):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


def solve_part1(data: list[str]):
    stars = get_stars(data)

    empt_rows = get_empt_rows(data)
    empt_cols = get_empt_col(data)
    added_rows = 0
    for row in empt_rows:
        for star in stars:
            if star[0] > row + added_rows:
                star[0] += 1
        added_rows += 1

    added_cols = 0
    for col in empt_cols:
        for star in stars:
            if star[1] > col + added_cols:
                star[1] += 1
        added_cols += 1

    sum_of_dist = 0
    perm = permutations(stars, 2)
    for p1, p2 in perm:
        sum_of_dist += get_distance(p1, p2)
    return sum_of_dist // 2


def solve_part2(data: list[str]):
    factor = 1_000_000
    stars = get_stars(data)
    empt_rows = get_empt_rows(data)
    empt_cols = get_empt_col(data)

    added_rows = 0
    for row in empt_rows:
        for star in stars:
            if star[0] > row + added_rows:
                star[0] += 1 * factor - 1
        added_rows += 1 * factor - 1

    added_cols = 0
    for col in empt_cols:
        for star in stars:
            if star[1] > col + added_cols:
                star[1] += 1 * factor - 1
        added_cols += 1 * factor - 1

    sum_of_dist = 0
    perm = permutations(stars, 2)
    for p1, p2 in perm:
        sum_of_dist += get_distance(p1, p2)
    return sum_of_dist // 2


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():
    day = 11

    data = read_data(f"d{day}_input.txt")
    # data = read_data(f"d{day}_sample.txt")

    start_time = time.perf_counter_ns()
    print(f"Solution Day {day}, Part1:")
    print(solve_part1(data))
    print(f"Time for part 1: {(time.perf_counter_ns()-start_time)/1000} ms")

    start_time = time.perf_counter_ns()
    print(f"Solution Day {day}, Part2:")
    print(solve_part2(data))
    print(f"Time for part 2: {(time.perf_counter_ns()-start_time)/1000} ms")


if __name__ == "__main__":
    main()
