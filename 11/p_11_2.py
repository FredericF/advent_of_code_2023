import typing as t
import numpy as np

from p_11_1 import t_dat, dat
from itertools import combinations


def get_galaxies(data: list[str], growth: int) -> t.Any:
    tmp = np.array([list(line) for line in data], dtype=str)
    rows, cols = np.where(tmp == "#")
    empty_rows = np.where(np.all(tmp == ".", axis=1))
    empty_cols = np.where(np.all(tmp == ".", axis=0))
    original_pos = zip(rows, cols)
    galaxies = []
    for row, col in original_pos:
        row = row + np.count_nonzero(empty_rows < row) * (growth - 1)
        col = col + np.count_nonzero(empty_cols < col) * (growth - 1)
        galaxies.append((row, col))
    return galaxies


def get_distance(galaxies: t.Any) -> int:
    pairs = combinations(galaxies, 2)
    return sum([abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) for g1, g2 in pairs])


def main() -> None:
    t10_galaxies = get_galaxies(t_dat, 10)
    t100_galaxies = get_galaxies(t_dat, 100)
    galaxies = get_galaxies(dat, 1000000)
    print(f"Distance for growth rate 10: {get_distance(t10_galaxies)}; expected: 1030")
    print(
        f"Distance for growth rate 100: {get_distance(t100_galaxies)}; expected: 8410"
    )
    print(f"{get_distance(galaxies)}")
    # 406725732046


if __name__ == "__main__":
    main()
