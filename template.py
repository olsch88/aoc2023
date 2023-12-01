def solve_part1(data: list[int]):
    return 0


def solve_part2(data: list[int]):
    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()

    return data


def main():
    day = 1

    data = read_data(f"d{day}_input.txt")

    print(f"Solution Day {day}, Part1:")
    print(solve_part1(data))
    print(f"Solution Day {day}, Part2:")
    print(solve_part2(data))


if __name__ == "__main__":
    main()
