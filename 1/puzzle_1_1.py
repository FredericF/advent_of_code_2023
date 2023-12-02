import re

with open("data.txt") as f:
    data = f.read().splitlines()

digits = [re.sub("[a-zA-Z]", "", line) for line in data]
numbers = [ int(line[0] + line[-1]) for line in digits]

print( sum(numbers))
