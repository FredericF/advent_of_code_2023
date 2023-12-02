import re

with open("data.txt") as f:
    data = f.read().splitlines()

test_data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

def main():
    digits = [re.sub("[a-zA-Z]", "", line) for line in data]
    numbers = [int(line[0] + line[-1]) for line in digits]
    print(sum(numbers))

if __name__ == "__main__":
    main()