from puzzle_4_1 import get_cards, test_data, data
import numpy as np

def get_total_cards(cards):
    counter = np.full(len(cards), 1)
    total = np.full(len(cards), 0)
    for i in range(len(cards)):
        if i == 0:
            total[i] = counter[i]
        else:
            total[i] = counter[i] + total[i - 1]
        counter[i + 1 : min(len(cards), i + 1 + cards["match_count"][i])] += counter[i]
    return total[-1]


def main():
    test_cards = get_cards(test_data)
    print(
        f"Total cards from test data is: {get_total_cards(test_cards)} ; expected: 30"
    )
    
    cards = get_cards(data)
    print(f"Total cards from data is: {get_total_cards(cards)}")


if __name__ == "__main__":
    main()
