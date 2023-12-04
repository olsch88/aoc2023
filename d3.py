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


def analyse_star(data: list[str], linenumber: int, star_index: int) -> int:
    """analyse the surrondig area of a star.
    returns the gear ration if it has two neibours
    returns 0 otherwise"""
    adjecent_number_count = 0
    gear_ratio = 1
    num_pattern = r"\d+"
    num_search = re.compile(num_pattern)
    # search for near numbers in line above:
    if linenumber > 0:
        for match in num_search.finditer(data[linenumber - 1]):
            if star_index in range(match.start() - 1, match.end() + 1):
                print(match.group())
                adjecent_number_count += 1
                gear_ratio *= int(match.group())
    # search for near numbers in line below:
    if linenumber < len(data) - 1:
        for match in num_search.finditer(data[linenumber + 1]):
            if star_index in range(match.start() - 1, match.end() + 1):
                # print(match.group())
                adjecent_number_count += 1
                gear_ratio *= int(match.group())
                print(match.group())
    # search for near numbers in current line
    for match in num_search.finditer(data[linenumber]):
        if match.start() == star_index + 1 or match.end() == star_index:
            print(match.group())
            adjecent_number_count += 1
            gear_ratio *= int(match.group())

    if adjecent_number_count != 2:
        return 0
    return gear_ratio


def solve_part2(data: list[str]):
    star_pattern = r"\*"
    star_search = re.compile(star_pattern)
    total_gear_ratio = 0
    for i, line in enumerate(data):
        for match in star_search.finditer(line):
            star_index = match.start()
            assert line[star_index] == "*"
            total_gear_ratio += analyse_star(data, i, star_index)

    return total_gear_ratio


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()

    return data


def main():
    day = 3

    data = read_data(f"d{day}_input.txt")
    # data = read_data(f"d{day}_sample2.txt")

    print(f"Solution Day {day}, Part1:")
    print(solve_part1(data))
    print(f"Solution Day {day}, Part2:")
    print(solve_part2(data))


if __name__ == "__main__":
    main()
