import numpy as np


class Card:
    def __init__(self, number: int):
        self._number = number
        self._numbers, self._winning = None, None

    def add_numbers(self, numbers: list):
        self._numbers = numbers

    def add_winning_numbers(self, winning_numbers: list):
        self._winning = winning_numbers

    def get_points(self) -> tuple:
        nb_winning_nbs = 0
        for win in self._winning:
            if win in self._numbers:
                nb_winning_nbs += 1
        if nb_winning_nbs > 0:
            return 2 ** (nb_winning_nbs - 1), nb_winning_nbs
        return 0, nb_winning_nbs


def load_data(filename: str) -> list:
    loaded_cards = []
    with open(filename, "r", encoding="utf8") as file_open:
        lines = file_open.readlines()

    for line in lines:
        loaded_card = line.rstrip().split(": ")[0]
        new_card = Card(int(loaded_card.split(" ")[-1]))
        numbers = line.rstrip().split(": ")[-1]
        own_numbers_list, winning_numbers_list = numbers.split(" | ")
        own_numbers, winning_numbers = [], []
        for number in own_numbers_list.split(" "):
            if number.isdigit():
                own_numbers.append(int(number))
        new_card.add_numbers(own_numbers)
        for number in winning_numbers_list.split(" "):
            if number.isdigit():
                winning_numbers.append(int(number))
        new_card.add_winning_numbers(winning_numbers)
        loaded_cards.append(new_card)
    return loaded_cards


if __name__ == "__main__":
    cards = load_data("../data/day04.txt")

    # part 1
    POINTS_PART1 = 0
    for card in cards:
        points, _ = card.get_points()
        POINTS_PART1 += points
    print(f"Part 1: {POINTS_PART1}")

    # part 2
    multiplier = np.ones(len(cards))
    for idx, card in enumerate(cards):
        _, wins = card.get_points()
        for i in range(wins):
            if i + idx + 1 < len(cards):
                multiplier[idx + i + 1] += multiplier[idx] * 1
    POINTS_PART2 = np.sum(multiplier)
    print(f"Part 2: {int(POINTS_PART2)}")
