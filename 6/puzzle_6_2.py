from puzzle_6_1 import data, test_data, Race
import numpy as np
from dataclasses import dataclass
import math
import re

@dataclass
class Race:
    time: int
    dist: int

    @property
    def ways_to_win(self):
        roots = np.roots([1, -self.time, -self.dist])

    @property
    def no_brute_force(self):
        roots = np.roots([1, -self.time, self.dist])
        return int( math.floor(max(roots)) - math.ceil(min(roots))  + 1)

def get_real_race(data):
    time = int(re.sub(r"\D+", '', data[0]))
    distance = int(re.sub(r"\D+", '', data[1]))
    return Race(time, distance)


def main():
    test_race = get_real_race(test_data)
    race = get_real_race(data)
    print(f"No brute force today. test race: {test_race.no_brute_force}; expected: 71503")
    print(f"real race: {race.no_brute_force}")

if __name__ == "__main__":
    main()