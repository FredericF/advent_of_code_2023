from puzzle_2_1 import data, test_data, red_re, blue_re, green_re

def power(game):
    red_max = max(int(x) for x in red_re.findall(game))
    blue_max = max(int(x) for x in blue_re.findall(game))
    green_max = max(int(x) for x in green_re.findall(game))
    return red_max * blue_max * green_max


def main():   
    print(f"Results on test data are: {[power(game) for game in test_data]}")
    print(f"Expected results = 48, 12, 1560, 630, 36")
    res = sum(power(game) for game in data)
    print(f"Sum of powers is: {res}")

if __name__ == "__main__":
    main()