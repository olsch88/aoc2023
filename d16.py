import time
from collections import deque
from typing import NewType

Position = NewType("Position", tuple[int, int])
Direction = NewType("Direction", tuple[int, int])
LightState = NewType("LightState", dict[str, tuple[int, int]])


def traverse_maze(grid: list[str], start=((0, 0), (0, 1))):
    queue = deque()
    visited = set()
    seen_positions = set()
    # start = {"pos": (0, 0), "dir": (0, 1)}
    # the first tuple contains the current position, the second tuple contains the current direction
    queue.append(start)
    while True:
        try:
            current_state = queue.popleft()
        except IndexError:  # queue is empty
            break
        if current_state in seen_positions:
            continue

        pos = current_state[0]
        dire = current_state[1]
        # edge cases:
        if pos[0] < 0 or pos[0] >= len(grid):
            continue
        if pos[1] < 0 or pos[1] >= len(grid[0]):
            continue

        visited.add(current_state[0])
        seen_positions.add(current_state)

        if grid[pos[0]][pos[1]] == ".":
            queue.append(((pos[0] + dire[0], pos[1] + dire[1]), dire))

        elif grid[pos[0]][pos[1]] == "\\":
            queue.append(((pos[0] + dire[1], pos[1] + dire[0]), (dire[1], dire[0])))

        elif grid[pos[0]][pos[1]] == "/":
            queue.append(
                (
                    (pos[0] - dire[1], pos[1] - dire[0]),
                    (-dire[1], -dire[0]),
                )
            )

        elif grid[pos[0]][pos[1]] == "|":
            if dire == (0, 1) or dire == (0, -1):
                queue.append(((pos[0] + 1, pos[1]), (1, 0)))
                queue.append(((pos[0] - 1, pos[1]), (-1, 0)))
            else:
                queue.append(((pos[0] + dire[0], pos[1] + dire[1]), dire))

        elif grid[pos[0]][pos[1]] == "-":
            if dire == (1, 0) or dire == (-1, 0):
                queue.append(((pos[0], pos[1] + 1), (0, 1)))
                queue.append(((pos[0], pos[1] - 1), (0, -1)))
            else:
                queue.append(((pos[0] + dire[0], pos[1] + dire[1]), dire))

    return len(visited)


def solve_part1(data: list[str]):
    return traverse_maze(data)


def solve_part2(data: list[str]):
    max_energy = 0
    for i in range(len(data)):
        current_energy = traverse_maze(data, start=((i, 0), (0, 1)))
        if current_energy > max_energy:
            max_energy = current_energy
        current_energy = traverse_maze(data, start=((i, len(data[0]) - 1), (0, -1)))
        if current_energy > max_energy:
            max_energy = current_energy

    for i in range(len(data[0])):
        current_energy = traverse_maze(data, start=((0, i), (1, 0)))
        if current_energy > max_energy:
            max_energy = current_energy
        current_energy = traverse_maze(data, start=((len(data) - 1, i), (-1, 0)))
        if current_energy > max_energy:
            max_energy = current_energy
    return max_energy


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():
    day = 16

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
