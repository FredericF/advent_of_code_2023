import re
import typing as t

with open("./12/test_data.txt", "r") as f:
    t_dat = f.read().splitlines()

with open("./12/data.txt", "r") as f:
    dat = f.read().splitlines()


def parse_data(data: list[str]) -> t.Any:
    rec_re = re.compile(r"(?P<pipes>[#\?\.]*)\s+(?P<groups>([\d]+,?)*)")
    records = []
    for line in data:
        m = rec_re.match(line)
        if m:
            pipes = m.group("pipes")
            groups = [int(group) for group in m.group("groups").split(",")]
            records.append((pipes, groups))
        else:
            print(f"could not parse {line=}")
    return records


def get_combinations(rec: t.Any) -> list[str]:
    for pipes, groups in rec:
        # regex = "".join([r"(?=([#\?]{" + str(group) + "}))[\.\?]+" for group in groups])
        regex = re.compile(r"(?=[\.\?][#\?]{3})(?=[\.\?]+[#\?]{2})(?=[\.\?]+[#\?]{1})R")
        matches = tuple(regex.finditer(pipes))
        # print(*matches)
        # regex = regex[:-7] # I dont want the last
        # print(regex) 
        # matches = tuple(re.finditer(regex, pipes))
        print(len(matches))


def main():
    t_records = parse_data(t_dat)
    get_combinations(t_records)


if __name__ == "__main__":
    main()

    # "?????#?#?.?#?#. 7,3"
