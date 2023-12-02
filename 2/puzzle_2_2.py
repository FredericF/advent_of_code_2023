import re

with open("data.txt") as f:
    data = f.read().splitlines()

red_re = re.compile(r"(?:(\d+) red)")
green_re = re.compile(r"(?:(\d+) green)")
blue_re = re.compile(r"(?:(\d+) blue)")
id_re = re.compile(r"(?:Game\s+(\d+):)")


def power(game):
    red_max = max(int(x) for x in red_re.findall(game))
    blue_max = max(int(x) for x in blue_re.findall(game))
    green_max = max(int(x) for x in green_re.findall(game))
    return red_max * blue_max * green_max

res = sum(power(game) for game in data)
print(res)

# Testing
test_data = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]
print(f"Results on test data are: {[power(game) for game in test_data]}")
print(f"Expected results = 48, 12, 1560, 630, 36")