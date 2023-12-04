import re

SYMBOLS = r"+=-*#$@/%&"


def solve_part1(data: list[str]):
    pattern = r"\d+"
    search = re.compile(pattern)
    sum_of_components = 0
    max_row = len(data) - 1
    max_col = len(data[0]) - 1  # asuming it is not jagged

    for i, line in enumerate(data):
        for match in search.finditer(line):
            start = match.start()
            stop = match.end()
            # next we get th surronding string from above, in the current line, and below
            surrondings = ""
            line_above = data[max(i - 1, 0)][max(start - 1, 0) : min(stop + 1, max_col)]
            current_line = line[max(start - 1, 0) : min(stop + 1, max_col)]
            line_below = data[min(i + 1, max_row)][
                max(start - 1, 0) : min(stop + 1, max_col)
            ]
            surrondings = line_above + current_line + line_below
            if any([c in SYMBOLS for c in surrondings]):
                sum_of_components += int(match.group())

    return sum_of_components


def solve_part2(data: list[str]):
    star_pattern = r"\*"
    star_search = re.compile(star_pattern)
    num_pattern = r"\d+"
    num_search = re.compile(num_pattern)

    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()

    return data


def main():
    day = 3

    data = read_data(f"d{day}_input.txt")
    data = read_data(f"d{day}_sample.txt")

    print(f"Solution Day {day}, Part1:")
    print(solve_part1(data))
    print(f"Solution Day {day}, Part2:")
    print(solve_part2(data))


if __name__ == "__main__":
    main()
