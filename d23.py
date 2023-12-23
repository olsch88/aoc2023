import time
from collections import deque
from pprint import pprint
from copy import deepcopy

neighbors = ((-1, 0), (1, 0), (0, -1), (0, 1))


def get_valid_neighbors(grid: list[str]) -> dict[tuple, list]:
    valid_neighbors = dict()
    valid_neighbors[(0, 1)] = [(1, 0)]
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            neighs = []
            for neigh in neighbors:
                if grid[row + neigh[0]][col + neigh[1]] != "#":
                    neighs.append(neigh)
            valid_neighbors[(row, col)] = neighs
    # pprint(valid_neighbors)
    return valid_neighbors


def traverse_maze(grid: list[str], start: tuple = (0, 1), end=(22, 21), part2=False):
    hike_lengths = []
    visited = []
    neighbors = get_valid_neighbors(grid)
    queue = deque()
    # every entry will consist of:
    # the current position,
    # the current direction
    # the current length,
    # the visited nodes along this path
    queue.append((start, (1, 0), 0, [(0, 1)]))
    while True:
        try:
            cur_pos, cur_dir, cur_len, visited = queue.popleft()
        except IndexError:
            break

        visited.append(cur_pos)

        if cur_pos == end:
            hike_lengths.append(cur_len)
            print(f"Found path with length {cur_len}")
            continue
        cur_len += 1
        if grid[cur_pos[0]][cur_pos[1]] == ">" and cur_dir == (0, -1) and not part2:
            # we cant walk in this direction, dead end
            continue

        if grid[cur_pos[0]][cur_pos[1]] == "v" and cur_dir == (-1, 0) and not part2:
            # we cant walk in this direction, dead end
            continue

        for neigh in neighbors[cur_pos]:
            if (cur_pos[0] + neigh[0], cur_pos[1] + neigh[1]) not in visited:
                queue.appendleft(
                    (
                        (cur_pos[0] + neigh[0], cur_pos[1] + neigh[1]),
                        neigh,
                        cur_len,
                        visited[:],
                    )
                )
    # print(f"Number of valid paths: {len(hike_lengths)}")
    return hike_lengths


def solve_part1(data: list[str]):
    width = len(data[0])
    height = len(data)
    lengths = traverse_maze(data, start=(0, 1), end=(height - 1, width - 2))
    # lengths = traverse_maze(data, start=(0, 1), end=(1, 1))
    # print(lengths)
    return max(lengths)


def solve_part2(data: list[str]):
    width = len(data[0])
    height = len(data)
    lengths = traverse_maze(data, start=(0, 1), end=(height - 1, width - 2), part2=True)
    # print(lengths)
    return max(lengths)


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():
    day = 23

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
