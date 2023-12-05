import re
from dataclasses import dataclass

with open("./5/data.txt") as f:
    data = f.read()

with open("5./test_data.txt") as f:
    test_data = f.read()


@dataclass
class Rule:
    dest: int
    source: int
    length: int

    def transform(self, input):
        if input >= self.source and input < (self.source + self.length):
            return self.dest + input - self.source
        else:
            return False


@dataclass
class Map:
    rules: list[Rule]

    def transform(self, input):
        for rule in self.rules:
            if rule.transform(input):
                return rule.transform(input)
        return input


@dataclass
class MapSet:
    maps: list[Map]

    def transform(self, input):
        for map in self.maps:
            input = map.transform(input)
        return input


def get_data(data):
    seed_re = re.compile(r"(?:seeds:\s+(?P<seeds>[0-9 ]*)\n\n)")
    seed_m = seed_re.search(data)
    seeds = [int(num) for num in re.split(r"\s+", seed_m.groups("seeds")[0])]
    map_re = re.compile(r"(?:map:\n(?P<map>([0-9 ]*|\n{1})*)\n\n)")
    maps = []
    for match in map_re.finditer(data):
        map = match.groups("map")[0].split("\n")
        map = [Rule(*[int(el) for el in re.split(r"\s+", line)]) for line in map]
        maps.append(Map(map))
    return {"seeds": seeds, "maps": MapSet(maps)}


def main():
    test = get_data(test_data)
    test_locations = [test["maps"].transform(seed) for seed in test["seeds"]]
    print(test_locations)
    print(f"Min location is: {min(test_locations)}; expected is 35.")

    d = get_data(data)
    print(min([d["maps"].transform(seed) for seed in d["seeds"]]))
    print("Expected: 324724204")


if __name__ == "__main__":
    main()
