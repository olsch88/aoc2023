import itertools


def get_mapping(data: list[str]):
    mappings: list[list[str]]
    mappings = []
    current_mapping = []
    for i, line in enumerate(data):
        if i <= 2:
            continue
        if line == "":
            continue
        if line[0].isdigit():
            current_mapping.append(line)
            continue
        elif line[0].islower():
            mappings.append(current_mapping)
            current_mapping = []
            continue
    mappings.append(current_mapping)
    return mappings


def get_seeds(data: list[str]) -> list[int]:
    return [int(i) for i in data[0].split(":")[1].strip().split(" ")]


def process_mapping(mapping: list[str], start_value: int) -> int:
    for line in mapping:
        dest_start, source_start, length = (int(i) for i in line.split())
        if start_value >= source_start and start_value <= (source_start + length):
            return start_value + dest_start - source_start

    return start_value


def get_seed_location(seed: int, mappings) -> int:
    next_value = seed
    # print(f"{seed} maps to ", end=" ")
    for mapping in mappings:
        next_value = process_mapping(mapping, next_value)
        # print(f"{next_value} maps to ", end=" ")
    # print()
    return next_value


def solve_part1(data: list[str]) -> int:
    mappings = get_mapping(data)
    seeds = get_seeds(data)
    min_location = 99999999999

    for seed in seeds:
        location = get_seed_location(seed, mappings)
        if location < min_location:
            min_location = location
    return min_location


def solve_part2(data: list[str]) -> int:
    mappings = get_mapping(data)
    seeds = get_seeds(data)
    min_location = 99999999999

    for i in range(0, len(seeds) - 1, 2):
        for s in range(seeds[i], seeds[i] + seeds[i + 1]):
            location = get_seed_location(s, mappings)
            if location < min_location:
                min_location = location
    return min_location

    # for seed in seeds:
    #     next_value = seed
    #     print(f"{seed} maps to ", end=" ")
    #     for mapping in mappings:
    #         next_value = process_mapping(mapping, next_value)
    #         print(f"{next_value} maps to ", end=" ")
    #     print()
    #     if next_value < min_location:
    #         min_location = next_value
    # return min_location


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]

    return data


def main():
    day = 5

    data = read_data(f"d{day}_input.txt")
    # data = read_data(f"d{day}_sample.txt")

    print(f"Solution Day {day}, Part1:")
    print(solve_part1(data))
    print(f"Solution Day {day}, Part2:")
    print(solve_part2(data))


if __name__ == "__main__":
    main()
