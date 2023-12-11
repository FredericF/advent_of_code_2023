import numpy as np
import typing as t
import re
from itertools import combinations

with open("./11/test_data.txt") as f:
    t_dat = f.read().splitlines()

with open("./11/data.txt") as f:
    dat = f.read().splitlines()


def create_universe(data: list[str]) -> t.Any:
    tmp = np.empty([0, len(data[0])], dtype=str)
    for i in range(len(data)):
        if re.search(r"#", data[i]):
            tmp = np.append(arr=tmp, values=[list(data[i])], axis=0)
        else:
            tmp = np.append(arr=tmp, values=[list(data[i]), list(data[i])], axis=0)
    res = np.copy(tmp)
    for i in reversed(range(len(res[0,:]))): 
        if not re.search(r"#", "".join(res[:,i])):
            res = np.insert(arr=res, obj=i, values=np.transpose(["."] * len(tmp[:,i])),  axis=1)
    return res


def get_distance(universe: t.Any):
    galaxies = zip(*(np.where(universe == "#")))
    pairs = combinations(galaxies, 2)
    return sum( [ abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) for g1, g2 in pairs ] )

def main() -> None:
    t_universe = create_universe(t_dat)
    print(get_distance(t_universe))
    universe = create_universe(dat)
    print(get_distance(universe))

if __name__ == "__main__":
    main()
