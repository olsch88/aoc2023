import re
import time


def solve_part1(data: list[str]) -> int:
    total = 0
    c: str
    first = ""
    last = ""
    for line in data:
        for c in line:
            if c.isdigit():
                first = c
                break
        for c in line[::-1]:
            if c.isdigit():
                last = c
                break
        # print(first)
        # print(last)
        total += int(first + last)
    return total


def solve_part2(data: list[str]) -> int:
    new_list = []
    digits_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for line in data:
        min_index = 999
        first = ""
        max_index = -1
        last = ""
        for number in digits_dict.keys():
            try:
                if (i := line.index(number)) < min_index:
                    min_index = i
                    first = number
            except ValueError:
                pass
            try:
                if (i := line.rindex(number)) > max_index:
                    max_index = i
                    last = number
            except ValueError:
                pass

        new_line = line
        for number_str in digits_dict.keys():
            new_line = new_line.replace(number_str, number_str + number_str)

        new_line = new_line.replace(first, digits_dict.get(first, ""), 1)
        new_line = new_line.replace(last, digits_dict.get(last, ""))
        new_list.append(new_line)

    return solve_part1(new_list)


def solve_part2_regex(data: list[str]) -> int:
    digits_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    total = 0
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    search = re.compile(pattern)

    for line in data:
        result = search.findall(line)
        subtotal = int(
            digits_dict.get(result[0], result[0])
            + digits_dict.get(result[-1], result[-1])
        )
        # print(result)
        # print(subtotal)
        total += subtotal

    return total


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()

    return data


def main():
    day = 1

    data = read_data(f"d{day}_input.txt")

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
