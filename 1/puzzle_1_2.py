import re

with open("data.txt") as f:
    data = f.read().splitlines()

searched = {
    "one": 1,    "1": 1,
    "two": 2,    "2": 2,
    "three": 3,    "3": 3,
    "four": 4,    "4": 4,
    "five": 5,    "5": 5,
    "six": 6,    "6": 6,
    "seven": 7,    "7": 7,
    "eight": 8,    "8": 8,
    "nine": 9,    "9": 9,
    "zero": 0,    "0": 0,
}


def get_res(line):
    found = {}
    for key in searched:
        first = line.find(key)
        last = line.rfind(key)
        if (first  != -1):
            found[first] = searched[key]
        if (last != -1):
            found[last] = searched[key]
    return str(found[min(found.keys())]) + str(found[max(found.keys())])

numbers = [ int(get_res(line)) for line in data]
# print(numbers)
print(sum(numbers))
