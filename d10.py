import time
from typing import NewType

Direction = NewType("Direction", tuple[int, int])

DIRECTIONS = {
    "North": (-1, 0),
    "South": (1, 0),
    "West": (0, -1),
    "East": (0, 1),
    "Nowhere": (0, 0),
}


def change_direction(current_element: str, previous_direction: Direction) -> Direction:
    if previous_direction == DIRECTIONS["West"]:
        if current_element == "-":
            return DIRECTIONS["West"]
        if current_element == "F":
            return DIRECTIONS["South"]
        if current_element == "L":
            return DIRECTIONS["North"]
    if previous_direction == DIRECTIONS["East"]:
        if current_element == "-":
            return DIRECTIONS["East"]
        if current_element == "7":
            return DIRECTIONS["South"]
        if current_element == "J":
            return DIRECTIONS["North"]
    if previous_direction == DIRECTIONS["North"]:
        if current_element == "|":
            return DIRECTIONS["North"]
        if current_element == "7":
            return DIRECTIONS["West"]
        if current_element == "F":
            return DIRECTIONS["East"]
    if previous_direction == DIRECTIONS["South"]:
        if current_element == "|":
            return DIRECTIONS["South"]
        if current_element == "J":
            return DIRECTIONS["West"]
        if current_element == "L":
            return DIRECTIONS["East"]

    return DIRECTIONS["Nowhere"]


def get_start_position(data: list[str]) -> tuple[int, int]:
    # Assumption: There is only one starting point
    for i, line in enumerate(data):
        if "S" in line:
            return (i, line.index("S"))
    return (0, 0)


def solve_part1(data: list[str]):
    # assumption: S has only two pipes leading to it. There is no second loop
    start_pos = get_start_position(data)
    new_positions = []
    for name, direct in DIRECTIONS.items():
        new_pos = (start_pos[0] + direct[0], start_pos[1] + direct[1])
        if (
            change_direction(data[new_pos[0]][new_pos[1]], direct)
            != DIRECTIONS["Nowhere"]
        ):
            new_positions.append(new_pos)
    print(new_positions)
    return 0


def solve_part2(data: list[str]):
    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():
    day = 10

    data = read_data(f"d{day}_input.txt")
    # data = read_data(f"d{day}_sample1.txt")
    # data = read_data(f"d{day}_sample2.txt")

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
