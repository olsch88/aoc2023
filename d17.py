import time
from pprint import pprint
from collections import deque


def find_shortest_path(
    grid: list[list[int]], start: tuple[int, int], end: tuple[int, int]
) -> int:
    """finds the shortest Distance from start to finish"""
    # extending the graph with a "wall" of visited places

    start = (start[0] + 1, start[1] + 1)
    end = (end[0] + 1, end[1] + 1)
    visited_grid = [
        [False for i in range(len(grid[0]) + 2)] for line in range(len(grid) + 2)
    ]
    for i in range(len(visited_grid)):
        visited_grid[i][0] = True
        visited_grid[i][len(visited_grid[0]) - 1] = True
    for i in range(len(visited_grid[0])):
        visited_grid[0][i] = True
        visited_grid[len(visited_grid) - 1][i] = True
    distances = [
        [999 for i in range(len(grid[0]) + 2)] for line in range(len(grid) + 2)
    ]

    new_grid = [[999 for i in line] for line in visited_grid]
    for r, row in enumerate(grid):
        for c, element in enumerate(row):
            new_grid[r + 1][c + 1] = grid[r][c]
    pprint(new_grid)
    grid = new_grid
    # pprint(visited_grid)
    distances[start[0]][start[1]] = 0
    print(f"end {end}")
    # every entry in the queue consists of
    # 1 .the current position
    # 2. the current direction
    # 3 the length of the current straight line
    queue = deque()
    queue.append((start, (0, 1), 0))
    queue.append((start, (1, 0), 0))
    while True:
        try:
            cur_pos, cur_dir, cur_len = queue.popleft()
        except IndexError:
            break
        # print(f"checking {cur_pos} {cur_dir} {cur_len}")
        # if cur_pos[0]+cur_dir[0]<0 or

        visited_grid[cur_pos[0]][cur_pos[1]] = True

        if distances[cur_pos[0] + cur_dir[1]][cur_pos[1] + cur_dir[0]] >= (
            distances[cur_pos[0]][cur_pos[1]]
            + grid[cur_pos[0] + cur_dir[1]][cur_pos[1] + cur_dir[0]]
        ):
            distances[cur_pos[0] + cur_dir[1]][cur_pos[1] + cur_dir[0]] = (
                distances[cur_pos[0]][cur_pos[1]]
                + grid[cur_pos[0] + cur_dir[1]][cur_pos[1] + cur_dir[0]]
            )

        if distances[cur_pos[0] - cur_dir[1]][cur_pos[1] - cur_dir[0]] >= (
            distances[cur_pos[0]][cur_pos[1]]
            + grid[cur_pos[0] - cur_dir[1]][cur_pos[1] - cur_dir[0]]
        ):
            distances[cur_pos[0] - cur_dir[1]][cur_pos[1] - cur_dir[0]] = (
                distances[cur_pos[0]][cur_pos[1]]
                + grid[cur_pos[0] - cur_dir[1]][cur_pos[1] - cur_dir[0]]
            )

        if cur_len < 3:
            if distances[cur_pos[0] + cur_dir[0]][cur_pos[1] + cur_dir[1]] >= (
                distances[cur_pos[0]][cur_pos[1]]
                + grid[cur_pos[0] + cur_dir[0]][cur_pos[1] + cur_dir[1]]
            ):
                distances[cur_pos[0] + cur_dir[0]][cur_pos[1] + cur_dir[1]] = (
                    distances[cur_pos[0]][cur_pos[1]]
                    + grid[cur_pos[0] + cur_dir[0]][cur_pos[1] + cur_dir[1]]
                )

        if not visited_grid[cur_pos[0] + cur_dir[1]][cur_pos[1] + cur_dir[0]]:
            queue.append(
                (
                    (cur_pos[0] + cur_dir[1], cur_pos[1] + cur_dir[0]),
                    (cur_dir[1], cur_dir[0]),
                    1,
                )
            )

        if not visited_grid[cur_pos[0] - cur_dir[1]][cur_pos[1] - cur_dir[0]]:
            queue.append(
                (
                    (cur_pos[0] - cur_dir[1], cur_pos[1] - cur_dir[0]),
                    (-cur_dir[1], -cur_dir[0]),
                    1,
                )
            )

        if (
            cur_len < 3
            and not visited_grid[cur_pos[0] + cur_dir[0]][cur_pos[1] + cur_dir[1]]
        ):
            queue.append(
                (
                    (cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1]),
                    (cur_dir[0], -cur_dir[1]),
                    cur_len + 1,
                )
            )

    pprint(distances)
    return distances[end[0]][end[1]]


def solve_part1(data: list[list[int]]):
    pprint(data)
    width = len(data[0])
    height = len(data)
    print(find_shortest_path(data, (0, 0), (height - 1, width - 1)))
    return 0


def solve_part2(data: list[list[int]]):
    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [[int(i) for i in line.strip()] for line in data]
    return data


def main():
    day = 17

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
