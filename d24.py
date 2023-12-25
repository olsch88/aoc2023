import time
from pprint import pprint
from itertools import permutations


def sign(n: int | float) -> bool:
    if n >= 0:
        return True
    return False


def get_hail_data(data: list[str]) -> list[dict[str, int]]:
    hail_data = []
    for line in data:
        coordinates, directions = line.split("@")
        coordinates = [int(i) for i in coordinates.strip().split(",")]

        directions = [int(i) for i in directions.strip().split(",")]

        hail_data.append(
            {
                "px": coordinates[0],
                "py": coordinates[1],
                "pz": coordinates[2],
                "vx": directions[0],
                "vy": directions[1],
                "vz": directions[2],
            }
        )

    # pprint(hail_data)
    return hail_data


def solve_part1(data: list[str]):
    hail_data = get_hail_data(data)
    area_min = 200000000000000
    area_max = 400000000000000
    n_intersections = 0
    for line1, line2 in permutations(hail_data, 2):
        m1 = line1["vy"] / line1["vx"]
        n1 = line1["py"] - m1 * line1["px"]

        m2 = line2["vy"] / line2["vx"]
        n2 = line2["py"] - m2 * line2["px"]

        if m1 == m2:
            # lines run parallel
            # print("parallel:")
            # print(f"\t{line1}, {line2}")
            continue

        n_sum = n2 - n1
        m_sum = m1 - m2
        # (m1-m2)*x = n2-n1
        x_intersect = (n_sum) / m_sum
        y_intersect = m1 * x_intersect + n1

        if area_min <= x_intersect <= area_max and area_min <= y_intersect <= area_max:
            # check, if intersection is in the past
            if sign(x_intersect - line1["px"]) != sign(line1["vx"]):
                continue
            if sign(x_intersect - line2["px"]) != sign(line2["vx"]):
                continue
            if sign(y_intersect - line1["py"]) != sign(line1["vy"]):
                continue
            if sign(y_intersect - line2["py"]) != sign(line2["vy"]):
                continue

            # print(f"{line1}, {line2}")
            # print(x_intersect, y_intersect)
            n_intersections += 1

    return n_intersections // 2


def solve_part2(data: list[str]):
    return 0


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def main():
    day = 24

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
