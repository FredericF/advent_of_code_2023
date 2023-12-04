from puzzle_3_1 import data, test_data, get_nums_and_pos, return_engine_parts
import re
import numpy as np
import math


def get_star_positions(data):
    star_positions = []
    for i, line in enumerate(data):
        m = re.finditer(r"\*", line)
        for match in m:
            star_positions.append({"row": i, "col": match.start()})
    return star_positions


def get_gears(star, nums_and_pos, data_shape):
    mat = np.full(data_shape, False)
    mat[
        max(0, star["row"] - 1) : min(data_shape[0], star["row"] + 2),
        max(0, star["col"] - 1) : min(data_shape[1], star["col"] + 2),
    ] = True
    gear_parts = [
        return_engine_parts(num["number"], num["row"], num["range"], mat)
        for num in nums_and_pos
    ]
    gear_parts = np.array(gear_parts)
    if sum(gear_parts > 0) == 2:
        gear_parts[gear_parts == 0] = 1
        return math.prod(gear_parts)
    else:
        return 0


def main():
    # star_positions = get_star_positions(test_data)
    # nums_and_pos = get_nums_and_pos(test_data)
    # data_shape = (len(test_data), len(test_data[0]))
    # gear_parts = [get_gears(star, nums_and_pos, data_shape) for star in star_positions]
    # print(sum(gear_parts))
    star_positions = get_star_positions(data)
    nums_and_pos = get_nums_and_pos(data)
    data_shape = (len(data), len(data[0]))
    gear_parts = [get_gears(star, nums_and_pos, data_shape) for star in star_positions]
    print(sum(gear_parts))


if __name__ == "__main__":
    main()
