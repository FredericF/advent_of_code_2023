import numpy as np
import re

with open("./3/data.txt") as f:
    data = f.read().splitlines()

test_data = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]


def get_acceptance_matrix(data):
    height = len(data)
    width = len(data[0])
    mat = np.full((height, width), False)
    # Check every character and set acceptance matrix to true if symbol is found
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if re.match(r"[^0-9.]", char):
                mat[
                    max(0, i - 1) : min(height, i + 2),
                    max(0, j - 1) : min(width, j + 2),
                ] = True
    return mat


def get_nums_and_pos(data):
    nums_and_pos = []
    for i, line in enumerate(data):
        m = re.finditer(r"\d+", line)
        for match in m:
            nums_and_pos.append(
                {"number": match.group(), "row": i, "range": match.span()}
            )
    return nums_and_pos


def return_engine_parts(number, row, range, acceptance_matrix):
    if any(acceptance_matrix[row, range[0] : range[1]]):
        return int(number)
    else:
        return 0


def main():
    mat_test = get_acceptance_matrix(test_data)
    nums_test = get_nums_and_pos(test_data)
    print(
        sum(
            (
                return_engine_parts(
                    num["number"], num["row"], num["range"], mat_test
                )
                for num in nums_test
            )
        )
    )
    mat = get_acceptance_matrix(data)
    nums = get_nums_and_pos(data)
    print(
        sum(
            (
                return_engine_parts(num["number"], num["row"], num["range"], mat)
                for num in nums
            )
        )
    )   


if __name__ == "__main__":
    main()
