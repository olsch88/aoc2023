import time
from collections import deque

neighbors = ((-1, 0), (0, -1), (0, 1), (1, 0))


def get_start_position(grid: list[str]) -> tuple[int, int]:
    for row, line in enumerate(grid):
        for col, plot in enumerate(line):
            if plot == "S":
                return (row, col)
    return (0, 0)


def walk_plot(grid: list[str], start_pos=(0, 0), max_step=6) -> int:
    width = len(grid[0])
    height = len(grid)

    queue = deque()
    visited_on_even_days = set()
    visited_on_odd_days = set()
    visited_on_even_days.add(start_pos)
    points_to_check = set()
    # each element in th queue contains the current coordinates and the steps taken so far
    queue.append((start_pos, 0))
    while True:
        try:
            cur_pos, cur_steps = queue.popleft()
        except IndexError:
            break

        if cur_steps > max_step:
            continue
        if cur_steps % 2 == 0:
            visited_on_even_days.add(cur_pos)
            # print(len(queue))
        else:
            visited_on_odd_days.add(cur_pos)

        for neighbor in neighbors:
            if (
                grid[(cur_pos[0] + neighbor[0]) % height][
                    (cur_pos[1] + neighbor[1]) % width
                ]
                != "#"
                and ((cur_pos[0] + neighbor[0]), (cur_pos[1] + neighbor[1]))
                not in visited_on_even_days
                and ((cur_pos[0] + neighbor[0]), (cur_pos[1] + neighbor[1]))
                not in visited_on_odd_days
                and ((cur_pos[0] + neighbor[0]), (cur_pos[1] + neighbor[1]))
                not in points_to_check
            ):
                points_to_check.add(
                    ((cur_pos[0] + neighbor[0]), (cur_pos[1] + neighbor[1]))
                )
                queue.append(
                    (
                        ((cur_pos[0] + neighbor[0]), (cur_pos[1] + neighbor[1])),
                        cur_steps + 1,
                    )
                )

    if max_step % 2 == 0:
        return len(visited_on_even_days)

    return len(visited_on_odd_days)


def get_differences(numbers: list[int]) -> list[int]:
    diffs = []
    for i in range(1, len(numbers)):
        diffs.append(numbers[i] - numbers[i - 1])
    return diffs


def solve_part1(data: list[str]):
    start = get_start_position(data)
    pos_count = walk_plot(data, start, max_step=6)
    return pos_count


def solve_part2(data: list[str]):
    start = get_start_position(data)
    numbers = dict()

    for i in [10, 50, 1000]:
        numbers[i] = walk_plot(data, start, max_step=i)
    print(numbers)
    a1, a2, a3 = numbers.keys()
    b1, b2, b3 = numbers.values()
    a = -(a1 * b2 - a1 * b3 - a2 * b1 + a2 * b3 + a3 * b1 - a3 * b2) / (
        (a1 - a2) * (a1 - a3) * (a2 - a3)
    )

    b = (
        a1**2 * b2
        - a1**2 * b3
        - a2**2 * b1
        + a2**2 * b3
        + a3**2 * b1
        - a3**2 * b2
    ) / ((a1 - a2) * (a1 - a3) * (a2 - a3))
    c = (
        a1**2 * a2 * b3
        - a1**2 * a3 * b2
        - a1 * a2**2 * b3
        + a1 * a3**2 * b2
        + a2**2 * a3 * b1
        - a2 * a3**2 * b1
    ) / ((a1 - a2) * (a1 - a3) * (a2 - a3))

    y = a * 5000**2 + b * 5000 + c

    print(a)
    print(b)
    print(c)
    print(y)


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():
    day = 21

    data = read_data(f"d{day}_input.txt")
    data = read_data(f"d{day}_sample.txt")

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
