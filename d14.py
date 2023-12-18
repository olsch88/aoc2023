import time
from pprint import pprint
import copy


def extend_grid(data: list[list[str]]):
    # adding a soiid wa
    grid = copy.deepcopy(data)
    grid.insert(0, ["#"] * len(data[0]))
    grid.append(["#"] * len(data[0]))
    for line in grid:
        line.insert(0, "#")
        line.append("#")

    return grid


def tilt_north(grid: list[list[str]]):
    moved = True
    while moved:
        moved = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "O":
                    if grid[row - 1][col] == ".":
                        grid[row - 1][col] = "O"
                        grid[row][col] = "."
                        moved = True


def tilt_south(grid: list[list[str]]):
    moved = True
    while moved:
        moved = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "O":
                    if grid[row + 1][col] == ".":
                        grid[row + 1][col] = "O"
                        grid[row][col] = "."
                        moved = True


def tilt_east(grid: list[list[str]]):
    moved = True
    while moved:
        moved = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "O":
                    if grid[row][col + 1] == ".":
                        grid[row][col + 1] = "O"
                        grid[row][col] = "."
                        moved = True


def tilt_west(grid: list[list[str]]):
    moved = True
    while moved:
        moved = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "O":
                    if grid[row][col - 1] == ".":
                        grid[row][col - 1] = "O"
                        grid[row][col] = "."
                        moved = True


def calc_load(grid: list[list[str]]):
    heigth = len(grid)
    total_load = 0
    for i, line in enumerate(grid, start=-1):
        subtotal = line.count("O") * (heigth - 2 - i)
        total_load += line.count("O") * (heigth - 2 - i)
    return total_load


def solve_part1(data: list[list[str]]):
    grid = extend_grid(data)
    # pprint(data)
    # pprint(grid)
    tilt_north(grid)
    # pprint(grid)

    return calc_load(grid)


def solve_part2(data: list[list[str]]):
    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [[c for c in line.strip()] for line in data]
    return data


def main():
    day = 14

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
