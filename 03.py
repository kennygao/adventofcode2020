import math
from itertools import count, starmap

with open("input/03.txt") as f:
    lines = [line.rstrip("\n") for line in f]

width = len(lines[0])


def trees(right, down):
    return sum(r[c % width] == "#" for r, c in zip(lines[::down], count(0, right)))


part1 = trees(3, 1)
print(f"{part1=}")

part2 = math.prod(starmap(trees, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
print(f"{part2=}")
