import numpy as np

with open("./9/test_data.txt") as f:
    t_dat = f.read().splitlines()

with open("./9/data.txt") as f:
    dat = f.read().splitlines()


def parse_data(data):
    splitted = [line.split(" ") for line in data]
    return [[int(num) for num in line] for line in splitted]


def next_in_list(seq):
    mat = np.full((len(seq), len(seq)), 0)
    mat[0, :] = seq
    for i in range(1, len(seq)):
        mat[i, i:] = mat[i - 1, i:] - mat[i - 1, (i - 1) : -1]
    return sum(mat[:, -1])


def main():
    t_seq = parse_data(t_dat)
    seq = parse_data(dat)
    t_total = sum([next_in_list(line) for line in t_seq])
    total = sum([next_in_list(line) for line in seq])
    print(f"Sum in test data: {t_total=}; expected is 114")
    print(f"Sum in data is {total}")


if __name__ == "__main__":
    main()
