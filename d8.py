import time
import itertools
import functools
import math

DIRECTION = {"L": 0, "R": 1}


def get_nodes(data: list[str]) -> dict[str, tuple[str, str]]:
    nodes = dict()
    for i, line in enumerate(data):
        if i < 2:
            continue
        key = line.split("=")[0].strip()
        value1 = line.split("=")[1].strip().strip("()").split(",")[0].strip()
        value2 = line.split("=")[1].strip().strip("()").split(",")[1].strip()
        nodes[key] = (value1, value2)

    return nodes


def solve_part1(data: list[str]):
    instructions = data[0].strip()
    nodes = get_nodes(data)

    path_length = 0
    curent_location = "AAA"
    for instr in itertools.cycle(instructions):
        curent_location = nodes[curent_location][DIRECTION[instr]]
        path_length += 1
        if curent_location == "ZZZ":
            return path_length
    return 0


def solve_part2(data: list[str]):
    instructions = data[0].strip()
    nodes = get_nodes(data)
    current_nodes = [node for node in nodes.keys() if node.endswith("A")]
    start_nodes = current_nodes[:]
    cycle_times = [0 for a in range(len(current_nodes))]
    nodes_seen = [[] for a in range(len(current_nodes))]
    path_length = -1
    next_nodes = []
    for j, instr in enumerate(itertools.cycle(instructions)):
        cur_inst_pos = j % len(instructions)
        path_length += 1
        for i, node in enumerate(current_nodes):
            next_node = nodes[node][DIRECTION[instr]]
            if next_node.endswith("Z"):
                cycle_times[i] = path_length + 1
            next_nodes.append(next_node)
        if all([node.endswith("Z") for node in next_nodes]):
            return path_length
        if all([n > 0 for n in cycle_times]):
            return math.lcm(*cycle_times))
        current_nodes = next_nodes
        next_nodes = []
    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():
    day = 8

    data = read_data(f"d{day}_input.txt")

    # data = read_data(f"d{day}_sample3.txt")

    start_time = time.perf_counter_ns()
    print(f"Solution Day {day}, Part1:")
    # print(solve_part1(data))
    print(f"Time for part 1: {(time.perf_counter_ns()-start_time)/1000} ms")

    start_time = time.perf_counter_ns()
    print(f"Solution Day {day}, Part2:")
    print(solve_part2(data))
    print(f"Time for part 2: {(time.perf_counter_ns()-start_time)/1000} ms")


if __name__ == "__main__":
    main()
