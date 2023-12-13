import re
import time


def get_wins(data: list[str]) -> dict[int, int]:
    wins = dict()
    for i, line in enumerate(data, start=1):
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

        wins[i] = len_intersect
    return wins


def solve_part1(data: list[str]):
    sum_of_scores = 0

    wins = get_wins(data)
    for num, win in wins.items():
        if win > 0:
            sum_of_scores += 2 ** (win - 1)

    return sum_of_scores


def solve_part2(data: list[str]) -> int:
    card_counts = {i: 1 for i in range(1, len(data) + 1)}
    wins = get_wins(data)
    for i, _ in enumerate(data, start=1):
        for w in range(wins[i]):
            card_counts[i + w + 1] += card_counts[i]

    scratchcards = sum(card_counts.values())

    return scratchcards


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():
    day = 4

    # data = read_data(f"d{day}_sample.txt")
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
