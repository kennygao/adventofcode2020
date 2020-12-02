import re

with open("input/02.txt") as f:
    lines = [line.rstrip("\n") for line in f]

pattern = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")


def valid1(line):
    lo, hi, letter, password = pattern.fullmatch(line).groups()
    return int(lo) <= password.count(letter) <= int(hi)


def valid2(line):
    lo, hi, letter, password = pattern.fullmatch(line).groups()
    return (password[int(lo) - 1] == letter) ^ (password[int(hi) - 1] == letter)


part1 = sum(valid1(line) for line in lines)
print(f"{part1=}")

part2 = sum(valid2(line) for line in lines)
print(f"{part2=}")
