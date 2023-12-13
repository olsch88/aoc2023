import time


def get_numbers(data: list[str]) -> list[list[int]]:
    new_data = []
    for line in data:
        new_data.append([int(n) for n in line.split()])
    return new_data


def get_differences(numbers: list[int]) -> list[int]:
    diffs = []
    for i in range(1, len(numbers)):
        diffs.append(numbers[i] - numbers[i - 1])
    return diffs


def solve_part1(data: list[str]):
    number_lines = get_numbers(data)
    sum_new_numbers = 0
    for line in number_lines:
        next_number = line[-1]
        next_dif_line = line.copy()
        while True:
            next_dif_line = get_differences(next_dif_line)
            next_number += next_dif_line[-1]
            if all([n == 0 for n in next_dif_line]):
                break
        sum_new_numbers += next_number

    return sum_new_numbers


def solve_part2(data: list[str]):
    number_lines = get_numbers(data)
    sum_new_numbers = 0
    for line in number_lines:
        next_dif_line = line.copy()
        new_lines = []
        while True:
            next_dif_line = get_differences(next_dif_line)
            new_lines.append(next_dif_line.copy())
            if all([n == 0 for n in next_dif_line]):
                break

        new_lines[-1].insert(0, 0)
        for i in range(len(new_lines) - 2, -1, -1):
            prev_value = new_lines[i][0] - new_lines[i + 1][0]

            new_lines[i].insert(0, prev_value)

        sum_new_numbers += line[0] - new_lines[0][0]

    return sum_new_numbers


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():
    day = 9

    data = read_data(f"d{day}_input.txt")
    # data = read_data(f"d{day}_sample.txt")

    start_time = time.perf_counter_ns()
    print(f"Solution Day {day}, Part1:")
    print(solve_part1(data))
    print(f"Time for part 1: {(time.perf_counter_ns()-start_time)/1000} µs")

    start_time = time.perf_counter_ns()
    print(f"Solution Day {day}, Part2:")
    print(solve_part2(data))
    # print(solve_part2([data[1]]))
    print(f"Time for part 2: {(time.perf_counter_ns()-start_time)/1000} µs")


if __name__ == "__main__":
    main()
