from puzzle_9_1 import t_dat, dat, parse_data
import numpy as np


def previous_in_list(seq: list[int]) -> int:
    mat = np.full((len(seq), len(seq)), 0)
    mat[0, :] = seq
    for i in range(1, len(seq)):
        mat[i, :-i] = mat[i - 1, 1 : (-(i - 1) or None)] - mat[i - 1, :-i]
    return sum(mat[::2, 0]) - sum(mat[1::2, 0])


def main():
    seq = parse_data(dat)
    t_total = sum([previous_in_list(line) for line in parse_data(t_dat)])
    total = sum([previous_in_list(line) for line in seq])
    print(f"Sum in test data: {t_total}; expected 2")
    print(f"Sum in data is {total}")


if __name__ == "__main__":
    main()
