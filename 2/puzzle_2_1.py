import re

with open("data.txt") as f:
    data = f.read().splitlines()

test_data = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

# using non capturing group with: (?: ... )
red_re = re.compile(r"(?:(\d+) red)")
green_re = re.compile(r"(?:(\d+) green)")
blue_re = re.compile(r"(?:(\d+) blue)")
id_re = re.compile(r"(?:Game\s+(\d+):)")

limits = {"red": 12, "green": 13, "blue": 14}

def is_valid(game):
    id = int(id_re.findall(game)[0])
    # Use findall to get a list of all 'color' numbers
    # Then use the "generator" syntax to transform strings into ints and get the max
    red_max = max(int(x) for x in red_re.findall(game))
    blue_max = max(int(x) for x in blue_re.findall(game))
    green_max = max(int(x) for x in green_re.findall(game))
    if (
        red_max > limits["red"]
        or blue_max > limits["blue"]
        or green_max > limits["green"]
    ):
        return 0
    else:
        return id

def main():
    print(f"Results on test data are: {[is_valid(game) for game in test_data]}")
    print(f"Expected results = 1, 2, 0, 0, 5")
    res = sum(is_valid(game) for game in data)
    print(f"Sum of IDs of valid games is: {res}")

if __name__ == "__main__":
    main() 