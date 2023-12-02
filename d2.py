import re


def get_id(line: str) -> int:
    pattern = r"Game \d*"
    search = re.compile(pattern)
    results = search.findall(line)
    id_number = int(results[0].split(" ")[1])
    return id_number


def get_color_count(line: str, color: str) -> list[int]:
    counts = []
    pattern = r"\d* " + color
    search = re.compile(pattern)

    result = search.findall(line)
    for res in result:
        counts.append(int(res.split(" ")[0]))
    return counts


def solve_part1(data: list[str]) -> int:
    max_red = 12
    max_green = 13
    max_blue = 14

    valid_id_sum = 0
    for line in data:
        if (
            all([b <= max_blue for b in get_color_count(line, "blue")])
            and all([g <= max_green for g in get_color_count(line, "green")])
            and all([r <= max_red for r in get_color_count(line, "red")])
        ):
            valid_id_sum += get_id(line)
    return valid_id_sum


def solve_part2(data: list[str]) -> int:
    power_sum = 0
    for line in data:
        power_sum += (
            max(get_color_count(line, "blue"))
            * max(get_color_count(line, "green"))
            * max(get_color_count(line, "red"))
        )

    return power_sum


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()

    return data


def main():
    day = 2
    data = read_data(f"d{day}_input.txt")

    print(f"Solution Day {day}, Part1:")
    print(solve_part1(data))
    print(f"Solution Day {day}, Part2:")
    print(solve_part2(data))


if __name__ == "__main__":
    main()
