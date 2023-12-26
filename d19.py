import time
import re
from pprint import pprint
from operator import gt, lt

operators = {">": gt, "<": lt}


def get_parts(data: list[str]) -> list[dict]:
    pattern = r"\d+"
    search = re.compile(pattern)
    parts = []
    for line in data:
        if line == "":
            continue
        if line[0] != "{":
            continue

        result = search.findall(line)
        parts.append(
            {
                "x": int(result[0]),
                "m": int(result[1]),
                "a": int(result[2]),
                "s": int(result[3]),
            }
        )

    return parts


def get_instructions(data: list[str]) -> dict:
    instructions = dict()
    for line in data:
        if line == "":
            break
        name, instr = line.split("{")
        instructions[name] = instr.strip("}").split(",")

    return instructions


def process_instruction(instruction, instructions: dict, part) -> bool:
    # returns true if part is accepted, false otherwise
    # print(instruction)
    if instruction == "A":
        return True
    if instruction == "R":
        return False

    workflow = instructions[instruction]

    for flow in workflow:
        if flow == "A":
            return True
        if flow == "R":
            return False
        if flow in instructions.keys():
            return process_instruction(flow, instructions, part)

        operator = operators[flow[1]]
        parameter = flow[0]
        check_value = int(flow.split(":")[0][2:])
        destination = flow.split(":")[1]

        if operator(part[parameter], check_value):
            return process_instruction(destination, instructions, part)

    return False


def solve_part1(data: list[str]):
    parts = get_parts(data)
    instructions = get_instructions(data)
    rating = 0
    for part in parts:
        if process_instruction("in", instructions, part):
            rating += part["x"] + part["m"] + part["a"] + part["s"]

    return rating


def solve_part2(data: list[str]):
    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():
    day = 19

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
