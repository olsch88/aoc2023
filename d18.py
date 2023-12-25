import time
from pprint import pprint
from collections import deque


# neighbors = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
neighbors = ((-1, 0), (0, -1), (0, 1), (1, 0))

directions_part2 = {0: "R", 1: "D", 2: "L", 3: "U"}


def get_directions(data: list[str]) -> list[tuple[str, int]]:
    instructions = []
    for line in data:
        dire, dist, _ = line.split()
        instructions.append((dire, int(dist)))
    return instructions


def decode_hex(data: list[str]) -> list[tuple[str, int]]:
    instructions = []
    for line in data:
        hex_code = line.split()[2].strip("(#)")

        distance = int(hex_code[:-1], base=16)
        direction = directions_part2[int(hex_code[-1])]

        instructions.append((direction, distance))

    return instructions


def shoelace_formula_tri(coordinates: list[tuple[int, int]]) -> int:
    sum_of_area = 0
    for i in range(len(coordinates) - 1):
        sum_of_area += (
            coordinates[i][1] * coordinates[i + 1][0]
            - coordinates[i + 1][1] * coordinates[i][0]
        )
    return abs(sum_of_area // 2)


def shoelace_formula_trap(coordinates: list[tuple[int, int]]) -> int:
    sum_of_area = 0
    for i in range(len(coordinates) - 1):
        sum_of_area += (coordinates[i][0] + coordinates[i + 1][0]) * (
            coordinates[i][1] - coordinates[i + 1][1]
        )
    return abs(sum_of_area // 2)


def get_coordinates(instructions: list[tuple[str, int]]) -> list[tuple[int, int]]:
    coordinates = []
    cur_pos = (0, 0)
    coordinates.append(cur_pos)
    for direction, length in instructions:
        if direction == "R":
            cur_pos = (cur_pos[0], cur_pos[1] + length)
            coordinates.append(cur_pos)
        if direction == "L":
            cur_pos = (cur_pos[0], cur_pos[1] - length)
            coordinates.append(cur_pos)
        if direction == "D":
            cur_pos = (cur_pos[0] + length, cur_pos[1])
            coordinates.append(cur_pos)
        if direction == "U":
            cur_pos = (cur_pos[0] - length, cur_pos[1])
            coordinates.append(cur_pos)

    return coordinates


def get_circumference(instructions: list[tuple[str, int]]) -> int:
    sum_length = 0
    for _, length in instructions:
        sum_length += length
    return sum_length


def bfs_content(circumference: set[tuple[int, int]]) -> int:
    queue = deque()
    visited = set()
    max_x = max([x for y, x in circumference])
    max_y = max([y for y, x in circumference])
    middle = (max_y // 2, max_x // 2)
    queue.append((1, 1))
    while True:
        try:
            cur_pos = queue.popleft()
        except IndexError:
            break
        visited.add(cur_pos)
        for neighbor in neighbors:
            if (
                cur_pos[0] + neighbor[0],
                cur_pos[1] + neighbor[1],
            ) not in circumference and (
                cur_pos[0] + neighbor[0],
                cur_pos[1] + neighbor[1],
            ) not in visited:
                queue.append((cur_pos[0] + neighbor[0], cur_pos[1] + neighbor[1]))
    return len(visited)


def solve_part1(data: list[str]):
    instructions = get_directions(data)
    dug_out = get_circumference(instructions)
    coordinates = get_coordinates(instructions)
    area = shoelace_formula_tri(coordinates)

    # pick's theorem
    return dug_out // 2 + area + 1


def solve_part2(data: list[str]):
    instructions = decode_hex(data)
    dug_out = get_circumference(instructions)
    coordinates = get_coordinates(instructions)
    area = shoelace_formula_tri(coordinates)
    # pick's theorem
    return dug_out // 2 + area + 1


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():
    day = 18

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
    main()
