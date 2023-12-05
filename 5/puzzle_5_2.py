from puzzle_5_1 import data, test_data, get_data


def expand_seeds(seeds):
    zipped = zip(seeds[::2], seeds[1::2])
    zipped = sorted(zipped)
    for i, j in zipped:
        for k in range(i, i + j):
            yield k


def expand_seeds_spaced(seeds, spacing):
    zipped = zip(seeds[::2], seeds[1::2])
    zipped = sorted(zipped)
    for i, j in zipped:
        for k in range(i, i + j, spacing):
            yield k


def main():
    test_d = get_data(test_data)
    print(min(test_d["maps"].transform(seed) for seed in expand_seeds(test_d["seeds"])))
    print("Expected: 46")

    d = get_data(data)

    minimum = float("inf")
    spacing = 10000
    target_seed = 0

    for seed in expand_seeds_spaced(d["seeds"], spacing):
        res = d["maps"].transform(seed)
        if res < minimum:
            minimum = res
            target_seed = seed
            print(f"Seed is {seed}, minimum is {minimum}")

    print(f"Refining search around {target_seed}")
    result_seed = target_seed

    for seed in expand_seeds(d["seeds"]):
        if seed < (target_seed - spacing):
            continue
        if seed > (target_seed + spacing):
            print("Finished refining.")
            break
        res = d["maps"].transform(seed)
        if res < minimum:
            minimum = res
            result_seed = seed
            print(f"Seed is {seed}, minimum is {minimum}")
    print(f"Final seed is {result_seed}, mininimum is {minimum}")


if __name__ == "__main__":
    main()
