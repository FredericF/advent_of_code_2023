from puzzle_7_1 import data, test_data, test2_data
from dataclasses import dataclass
from functools import total_ordering
import re
import numpy as np

card_values = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


@dataclass
@total_ordering
class Hand:
    cards: list[str]
    bet: int

    @property
    def modified_J(self):
        numJ = np.count_nonzero(np.array(list(self.cards)) == "J")
        if numJ == 0 or numJ == 5:
            return self.cards
        if numJ == 4:
            return ["A", "A", "A", "A", "A"]
       
        noJ = "".join(self.cards).replace("J", "")
        card, counts = np.unique(list(noJ), return_counts=True)
        max_index = np.argmax(counts)
        max_card = card[max_index]
        return list(re.sub(max_card, "J", "".join(self.cards)))

    @property
    def type(self):
        card, count = np.unique(self.modified_J, return_counts=True)
        count = sorted(count, reverse=True)
        type = count[0]
        if type == 3:
            if count[1] == 2:
                type = 3.5
        if type == 2:
            if count[1] == 2:
                type = 2.5
        return type

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        for i in range(5):
            if card_values[self.cards[i]] != card_values[other.cards[i]]:
                return card_values[self.cards[i]] < card_values[other.cards[i]]
        return False

    def __eq__(self, other):
        return self.cards == other.cards


@dataclass
class HandSet:
    hands: list[Hand]

    @property
    def winnings(self):
        sorted_hands = sorted(self.hands, reverse=False)
        return sum([(i + 1) * hand.bet for i, hand in enumerate(sorted_hands)])


def get_hand_set(data):
    hands = []
    for line in data:
        m = re.match(r"(?P<cards>[123456789AKQJT]{5})\s*(?P<bet>\d+)", line)
        if m:
            hands.append(Hand(list(m.group("cards")), int(m.group("bet"))))
        else:
            print(f"Could not parse line: '{line}'")
    return HandSet(hands)


def main():
    test_hands = get_hand_set(test_data)
    print(f"Winnings test hands = {test_hands.winnings}; expected 5905")
    test2_hands = get_hand_set(test2_data)
    print(f"Winnings test2 hands = {test2_hands.winnings}; expected 6839")
    hands = get_hand_set(data)
    print(f"Winning hads: {hands.winnings}")


if __name__ == "__main__":
    main()
