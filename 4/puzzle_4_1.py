import pandas as pd
import re
from dataclasses import dataclass, field

with open("./4/data.txt") as f:
    data = f.read().splitlines()

with open("./4/test_data.txt") as f:
    test_data = f.read().splitlines()


@dataclass
class Card:
    id: int = None
    winning_numbers: list[int] = field(default_factory=list)
    numbers: list[int] = field(default_factory=list)

    @property
    def match_count(self):
        return len(set(self.winning_numbers) & set(self.numbers))

    @property
    def value(self):
        return 2 ** (self.match_count - 1) if self.match_count > 0 else 0
    
    def to_dict(self):
        return {
            "id": self.id,
            "winning_numbers": self.winning_numbers,
            "numbers": self.numbers,
            "match_count": self.match_count,
            "value": self.value,
        }


def get_cards(data):
    cards = []
    card_re = re.compile(
        r"(?:Card\s+(?P<id>\d+):\s*(?P<winning_numbers>.+)\s+\|(?:\s+(?P<numbers>.+)))"
    )
    for line in data:
        m = card_re.match(line)
        id = int(m.group("id")) if m.group("id") else None
        winning_numbers = []
        numbers = []
        if m.group("winning_numbers"):
            nums = m.group("winning_numbers")
            winning_numbers = [int(num) for num in re.split(r"\s++", nums)]
        if m.group("numbers"):
            nums = m.group("numbers")
            numbers = [int(num) for num in re.split(r"\s++", nums)]
        card = Card(id=id, winning_numbers=winning_numbers, numbers=numbers)
        cards.append(card)
    return pd.DataFrame([card.to_dict() for card in cards])


def main():
    test_cards = get_cards(test_data)
    print(test_cards.head())
    print(f"Sum of test card value is : {sum(test_cards['value'])} ; expected: 13")

    cards = get_cards(data)
    print(cards.head())
    print(f"Sum of card data is: {sum(cards['value'])}")


if __name__ == "__main__":
    main()
