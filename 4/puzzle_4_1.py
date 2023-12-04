import pandas as pd
import re
from dataclasses import dataclass

with open("./4/data.txt") as f:
    data = f.read().splitlines()

with open("./4/test_data.txt") as f:
    test_data = f.read().splitlines()


@dataclass
class Card:
    id: int
    winning_numbers: list
    numbers: list
    match_count: int
    value: int
    # @property
    # def match_count(self):
    #     return len(set(self.winning_numbers) & set(self.numbers))

    # @property
    # def value(self):
    #     return 2 ** (self.match_count - 1) if self.match_count > 0 else 0


def get_cards(data):
    cards = []
    card_re = re.compile(
        r"(?:Card\s(?P<id>\d+):\s*(?P<winning_numbers>.+)\s+\|(?:\s+(?P<numbers>.+)))"
    )
    for line in data:
        card = Card(id=None, winning_numbers=[], numbers=[], match_count=0, value=0)
        m = card_re.match(line)
        if m.group("id"):
            card.id = int(m.group("id"))
        if m.group("winning_numbers"):
            nums = m.group("winning_numbers")
            card.winning_numbers = [int(num) for num in re.split(r"\s++", nums)]
        if m.group("numbers"):
            nums = m.group("numbers")
            card.numbers = [int(num) for num in re.split(r"\s++", nums)]
        card.match_count = len(set(card.winning_numbers) & set(card.numbers))
        card.value = 2 ** (card.match_count - 1) if card.match_count > 0 else 0
        cards.append(card)
    return cards


def main():
    cards = get_cards(test_data)
    print(cards[0].__dict__)
    toto = pd.DataFrame([card.__dict__ for card in cards])
    print(toto.head())
    print(sum(toto["value"]))


if __name__ == "__main__":
    main()
