import time
import itertools
import functools

from enum import auto, IntEnum


class HandType(IntEnum):
    HIGHCARD = 1
    ONEPAIR = 2
    TWOPAIR = 3
    THREEKIND = 4
    FULLHOUSE = 5
    FOURKIND = 6
    FIVEKIND = 7


CARDVALUES = {
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}
CARDVALUES_PART2 = {
    "T": 10,
    "J": 1,
    "Q": 12,
    "K": 13,
    "A": 14,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class Hand:
    def __init__(self, cards: str, part: int = 1) -> None:
        self.part = part
        self.cards = cards
        if part == 1:
            self.hand_type: HandType = get_hand_type(cards)
        else:
            self.hand_type: HandType = get_hand_type_part2(cards)

    def __eq__(self, other: "Hand") -> bool:
        if self.hand_type != other.hand_type:
            print(self.hand_type, other.hand_type)
            return False
        for a, b in zip(self.cards, other.cards):
            if CARDVALUES[a] != CARDVALUES[b]:
                return False

        return True

    def __gt__(self, other: "Hand") -> bool:
        if self.hand_type > other.hand_type:
            return True
        elif self.hand_type < other.hand_type:
            return False
        for a, b in zip(self.cards, other.cards):
            if self.part == 1:
                if CARDVALUES[a] > CARDVALUES[b]:
                    return True
                if CARDVALUES[a] < CARDVALUES[b]:
                    return False
            else:
                if CARDVALUES_PART2[a] > CARDVALUES_PART2[b]:
                    return True
                if CARDVALUES_PART2[a] < CARDVALUES_PART2[b]:
                    return False

        return False

    def __lt__(self, other: "Hand") -> bool:
        if self.hand_type < other.hand_type:
            return True
        elif self.hand_type > other.hand_type:
            return False
        for a, b in zip(self.cards, other.cards):
            if self.part == 1:
                if CARDVALUES[a] < CARDVALUES[b]:
                    return True
                if CARDVALUES[a] > CARDVALUES[b]:
                    return False
            else:
                if CARDVALUES_PART2[a] < CARDVALUES_PART2[b]:
                    return True
                if CARDVALUES_PART2[a] > CARDVALUES_PART2[b]:
                    return False
        return False

    def __hash__(self) -> int:
        return hash(str(self.hand_type) + self.cards)

    def __str__(self) -> str:
        return self.cards

    def __repr__(self) -> str:
        return self.cards


def get_hand_type(cards: str) -> HandType:
    for c in cards:
        if cards.count(c) == 5:
            return HandType.FIVEKIND
        if cards.count(c) == 4:
            return HandType.FOURKIND
        if cards.count(c) == 3:
            for d in cards:
                if d == c:
                    continue
                if cards.count(d) == 2:
                    return HandType.FULLHOUSE
            return HandType.THREEKIND
        if cards.count(c) == 2:
            for d in cards:
                if d == c:
                    continue
                if cards.count(d) == 3:
                    return HandType.FULLHOUSE
                if cards.count(d) == 2:
                    return HandType.TWOPAIR
            return HandType.ONEPAIR
    return HandType.HIGHCARD


def get_hand_type_part2(cards: str) -> HandType:
    for c in cards:
        if c == "J":
            if cards.count(c) == 5:
                return HandType.FIVEKIND
        if cards.count(c) + cards.count("J") == 5:
            return HandType.FIVEKIND
    for c in cards:
        if c == "J":
            continue
        if cards.count(c) + cards.count("J") == 4:
            return HandType.FOURKIND
    for c in cards:
        if c == "J":
            continue
        if cards.count(c) + cards.count("J") == 3:
            for d in cards:
                if d == c or d == "J":
                    continue
                if cards.count(d) == 2:
                    return HandType.FULLHOUSE
            return HandType.THREEKIND
    for c in cards:
        if c == "J":
            continue
        if cards.count(c) + cards.count("J") == 2:
            for d in cards:
                if d == c or d == "J":
                    continue
                if cards.count(d) == 3:
                    return HandType.FULLHOUSE
                if cards.count(d) == 2:
                    return HandType.TWOPAIR
            return HandType.ONEPAIR
    return HandType.HIGHCARD


def solve_part1(data: list[str]):
    hands = []

    for line in data:
        cards, bid = line.split()
        hands.append({"hand": Hand(cards), "bid": bid})
    hands = sorted(hands, key=lambda c: c["hand"])
    total_winnings = 0
    for rank, hand in enumerate(hands, start=1):
        total_winnings += rank * int(hand["bid"])

    return total_winnings


def solve_part2(data: list[str]):
    hands: list[dict] = []

    for line in data:
        cards, bid = line.split()
        hands.append({"hand": Hand(cards, part=2), "bid": bid})
    hands = sorted(hands, key=lambda c: c["hand"])
    total_winnings = 0
    for rank, hand in enumerate(hands, start=1):
        total_winnings += rank * int(hand["bid"])

    return total_winnings


def read_data(input_file: str):
    with open(input_file, "r") as file:
        data = file.readlines()
    data = [line.strip() for line in data]
    return data


def test_hand_types():
    assert get_hand_type("AA234") == HandType.ONEPAIR
    assert get_hand_type("AA223") == HandType.TWOPAIR
    assert get_hand_type("AA222") == HandType.FULLHOUSE
    assert get_hand_type("AAA22") == HandType.FULLHOUSE
    assert get_hand_type("AK222") == HandType.THREEKIND
    assert get_hand_type("AKKK2") == HandType.THREEKIND
    assert get_hand_type("AAAQ2") == HandType.THREEKIND
    assert get_hand_type("AAAA2") == HandType.FOURKIND
    assert get_hand_type("2AAAA") == HandType.FOURKIND
    assert get_hand_type("AAAAA") == HandType.FIVEKIND


def test_hand_types_part2():
    assert get_hand_type_part2("JJJAA") == HandType.FIVEKIND
    assert get_hand_type_part2("JJJJJ") == HandType.FIVEKIND
    assert get_hand_type_part2("AJJJJ") == HandType.FIVEKIND
    assert get_hand_type_part2("AAJJJ") == HandType.FIVEKIND
    assert get_hand_type_part2("JAJAJ") == HandType.FIVEKIND
    assert get_hand_type_part2("JJTTK") == HandType.FOURKIND
    assert get_hand_type_part2("JJT33") == HandType.FOURKIND
    assert get_hand_type_part2("JTT33") == HandType.FULLHOUSE
    assert get_hand_type_part2("TTJ33") == HandType.FULLHOUSE
    assert get_hand_type_part2("TTJ23") == HandType.THREEKIND
    assert get_hand_type_part2("TT223") == HandType.TWOPAIR
    assert get_hand_type_part2("AQTKJ") == HandType.ONEPAIR
    assert get_hand_type_part2("J444T") == HandType.FOURKIND
    assert get_hand_type_part2("JAAJA") == HandType.FIVEKIND
    assert get_hand_type_part2("483JJ") == HandType.THREEKIND


def test_compare_hands():
    assert Hand("AAAAA") == Hand("AAAAA")
    assert Hand("AAAAA") > Hand("AKQJT")
    assert Hand("KKKKK") < Hand("AAAAA")
    assert Hand("KKK22") > Hand("AAKK2")
    assert Hand("KKK22") < Hand("AAAKK")
    assert Hand("QQQJA") > Hand("32T3K")
    assert Hand("KK677") > Hand("KTJJT")
    assert Hand("KTJJT") < Hand("KK667")
    assert Hand("T55J5") < Hand("QQQJA")
    assert Hand("KK677") < Hand("T55J5")
    assert Hand("KTJJT") < Hand("QQQJA")


def main():
    day = 7

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
    test_hand_types()
    test_compare_hands()
    test_hand_types_part2()
    main()
