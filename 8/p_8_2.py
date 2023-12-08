from p_8_1 import dat, parse_map
import re
import math

with open("./8/test_data_2.txt", "r") as f:
    test_dat = f.read().splitlines()


def get_ghosts(data):
    ghosts = []
    for line in data[2:]:
        m = re.match(r"^(.{2}A)", line)
        if m:
            ghosts.append(m.group(1))
    return ghosts


def single_ghost(parsed_data, ghost):
    map, instruction = parsed_data["map"], parsed_data["instruction"]
    num_steps = 0
    node = ghost
    while True:
        step = instruction[num_steps % len(instruction)]
        node = map[node][step]
        num_steps += 1
        if node[2] == "Z":
            return num_steps


def ghost_navigate(parsed_data, ghosts):
    return math.lcm(*(single_ghost(parsed_data, ghost) for ghost in ghosts))


def main():
    t_ghosts = get_ghosts(test_dat)
    ghosts = get_ghosts(dat)
    t_map = parse_map(test_dat)
    map = parse_map(dat)

    print(f"{t_ghosts=}; {ghosts=}")
    print(
        f"Test data: num_steps = {ghost_navigate(t_map, t_ghosts)}; expected=6"
    )
    print(f"Data: num_steps = {ghost_navigate(map, ghosts)}")


if __name__ == "__main__":
    main()
