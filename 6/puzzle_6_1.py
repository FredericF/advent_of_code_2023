import re
import math
from dataclasses import dataclass

with open("./6/data.txt") as f:
    data = f.read().splitlines()

with open("./6/test_data.txt") as f:
    test_data = f.read().splitlines()


@dataclass
class Race:
    time: int
    dist: int

    @property
    def ways_to_win(self):
        return sum(i * (self.time - i) > self.dist for i in range(1, self.dist))


@dataclass
class RaceSet:
    races: list[Race]

    @property
    def ways_to_win(self):
        return math.prod( [race.ways_to_win for race in self.races] )


def get_race_set(data):
    times = [int(time) for time in re.split(r"\s+", data[0])[1:]]
    dists = [int(dist) for dist in re.split(r"\s+", data[1])[1:]]
    return RaceSet( [ Race(i,j) for i,j in zip(times, dists) ] )
    

def main():
    test_races = get_race_set(test_data)
    races = get_race_set(data)
    print(races)
    print(f"Ways to win test races = {test_races.ways_to_win}; expected 288")
    print(f"Ways to win races: {races.ways_to_win}")

if __name__ == "__main__":
    main()
