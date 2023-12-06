import time


def get_distance(max_time: int, start_time: int) -> int:
    distance = start_time * (max_time - start_time)
    # distance = start_time*max_time-start_time**2
    return distance


def get_min_time_from_distance(distance: int) -> int:
    return 0


def generate_input(data: list[str]) -> list[dict[str, int]]:
    times = [int(i) for i in data[0].split(":")[1].split()]
    distances = [int(i) for i in data[1].split(":")[1].split()]
    assert len(times) == len(distances)
    records = []
    for tim, dist in zip(times, distances):
        record = dict()
        record["Time"] = tim
        record["Distance"] = dist
        records.append(record)

    return records


def generate_input_part2(data: list[str]) -> dict[str, int]:
    times = [i for i in data[0].split(":")[1].split() if i.isdigit()]
    distances = [i for i in data[1].split(":")[1].split() if i.isdigit()]
    times = int("".join(times))
    distances = int("".join(distances))

    return {"Time": times, "Distance": distances}


def solve_part1(data: list[str]):
    records = generate_input(data)
    result = 1
    for record in records:
        count = 0
        for duration in range(0, record["Time"]):
            if get_distance(record["Time"], duration) > record["Distance"]:
                count += 1
        result *= count

    return result


def solve_part2(data: list[str]):
    record = generate_input_part2(data)

    count = 0
    for duration in range(0, record["Time"]):
        if get_distance(record["Time"], duration) > record["Distance"]:
            count += 1

    return count


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():
    day = 6

    data = read_data(f"d{day}_input.txt")
    # data = read_data(f"d{day}_sample.txt")

    start_time = time.perf_counter_ns()
    print(f"Solution Day {day}, Part1:")
    print(solve_part1(data))
    print(f"Time for part 1: {(time.perf_counter_ns()-start_time)/1000} ms")

    start_time = time.perf_counter_ns()
    print(f"Solution Day {day}, Part2:")
    print(solve_part2(data))
    print(f"Time for part 2: {(time.perf_counter_ns()-start_time)/1000} ms")


if __name__ == "__main__":
    main()
