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
    boxes: dict[int, list] = dict()
    focal_length = 0
    entry = ""

    for i in range(256):
        boxes[i] = []

    for instruction in data:
        # identify the target box
        if "-" in instruction:
            label = instruction[:-1]
        else:
            label = instruction.split("=")[0]

        box = hash_str(label)

        # fill the boxes
        if "-" in instruction:
            for i, element in enumerate(boxes[box]):
                if element.split()[0] == label:
                    boxes[box].remove(element)
                    break
        elif "=" in instruction:
            found_in_box = False
            focal_length = instruction.split("=")[1]
            entry = label + " " + focal_length
            for i, element in enumerate(boxes[box]):
                if element.split()[0] == label:
                    boxes[box][i] = entry
                    found_in_box = True
                    break
            if not found_in_box:
                boxes[box].append(entry)
    total = 0
    for number, box in boxes.items():
        for i, element in enumerate(box):
            total += (number + 1) * (i + 1) * int(element.split()[1])

    return total


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readline()
    return data.split(",")


data = read_data(f"d15_input.txt")


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
    main()
