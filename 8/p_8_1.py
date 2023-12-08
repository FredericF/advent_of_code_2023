import re

with open("./8/test_data.txt", "r") as f:
    test_dat = f.read().splitlines()

with open("./8/data.txt", "r") as f:
    dat = f.read().splitlines()


def parse_map(data):
    instructions = data[0]
    map = {}
    for line in data[2:]:
        m = re.match(
            r"(?P<ROOT>\w{3})\s+=\s+\((?P<L>\w{3}),\s+(?P<R>\w{3})", line
        )
        if m:
            map[m["ROOT"]] = {"L": m["L"], "R": m["R"]}
        else:
            print(f"Error parsing line: {line}")
    return {"instruction": instructions, "map": map}


def navigate(parsed_data):
    map, instruction = parsed_data["map"], parsed_data["instruction"]
    num_steps = 0
    node = "AAA"
    while True:
        step = instruction[num_steps % len(instruction)]
        num_steps += 1
        node = map[node][step]
        if node == "ZZZ":
            return num_steps


def main():
    test = parse_map(test_dat)
    print(f"Navigate on test data: num_steps = {navigate(test)} ; expected 6")
    data = parse_map(dat)
    print(f"Navigate on real data: num_steps = {navigate(data)}")


if __name__ == "__main__":
    main()
