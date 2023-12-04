import re


def solve_part1(data: list[str]):
    sum_of_scores = 0

    for line in data:
        winning_numbers = set()
        my_numbers = set()
        new_line = line.replace("  ", " ")
        parts = new_line.strip().split("|")
        numbers = parts[0].split(":")[1].strip().split(" ")
        for num in numbers:
            winning_numbers.add(int(num))
        numbers = parts[1].strip().split(" ")
        for num in numbers:
            my_numbers.add(int(num))
        len_intersect = len(winning_numbers.intersection(my_numbers))
        if len_intersect > 0:
            sum_of_scores += 2 ** (len_intersect - 1)

    return sum_of_scores


def solve_part2(data: list[str]):
    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():
    day = 4

    data = read_data(f"d{day}_sample.txt")
    data = read_data(f"d{day}_input.txt")

    print(f"Solution Day {day}, Part1:")
    print(solve_part1(data))
    print(f"Solution Day {day}, Part2:")
    print(solve_part2(data))


if __name__ == "__main__":
    main()
