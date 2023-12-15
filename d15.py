import time


def hash_str(str_to_hash: str) -> int:
    current_value = 0
    for c in str_to_hash:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256
    return current_value


def solve_part1(data: list[str]) -> int:
    total_hash = 0
    for element in data:
        total_hash += hash_str(element)
    return total_hash


def solve_part2(data: list[str]):
    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readline()
    return data.split(",")


def main():
    day = 15

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
    print(hash_str("qp"))
    main()
