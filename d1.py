def solve_part1(data: list[str]) -> int:
    total = 0
    c: str
    first = ""
    last = ""
    for line in data:
        for c in line:
            if c.isdigit():
                first = c
                break
        for c in line[::-1]:
            if c.isdigit():
                last = c
                break
        # print(first)
        # print(last)
        total += int(first + last)
    return total


def solve_part2(data: list[str]) -> int:
    new_list = []
    digits_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for line in data:
        min_index = 999
        first = ""
        max_index = 999
        last = ""
        print(line)
        for number in digits_dict.keys():
            try:
                if (i := line.index(number)) < min_index:
                    print(f"new_fist index {i} {number}")
                    min_index = i
                    first = number
            except ValueError:
                pass
            try:
                num = number[::-1]
                if (i := line[::-1].index(num)) < max_index:
                    print(f"new_last index {i} {number}")
                    max_index = i
                    last = number
            except ValueError:
                pass

        print(first)
        print(last)
        new_line = line.replace(first, digits_dict.get(first, ""), 1)
        new_line = new_line.replace(last, digits_dict.get(last, ""))
        new_list.append(new_line)
        print(new_line)

    return solve_part1(new_list)


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()

    return data


def main():
    day = 1

    data = read_data(f"d{day}_input.txt")
    # data = read_data("d1_p2_sample.txt")
    data = read_data("special.txt")

    print(f"Solution Day {day}, Part1:")
    print(solve_part1(data))
    print(f"Solution Day {day}, Part2:")
    print(solve_part2(data))


if __name__ == "__main__":
    main()
    # string = "abscece"
    # search = "xxxx"
    # ind = string.index(search)
    # print(ind)
