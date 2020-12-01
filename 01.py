import bisect
import math

with open("input/01.txt") as f:
    entries = [int(line.rstrip("\n")) for line in f]


def two_sum(ns, target):
    ns.sort()
    for i, n in enumerate(ns):
        j = bisect.bisect_left(ns, target - n, lo=i + 1)
        if j < len(ns) and ns[j] == target - n:
            return n, target - n


def three_sum(ns, target):
    ns.sort()
    for i, n in enumerate(ns):
        if ts := two_sum(ns[i + 1 :], target - n):
            return n, *ts


part1 = math.prod(two_sum(entries, 2020))
print(f"{part1=}")

part2 = math.prod(three_sum(entries, 2020))
print(f"{part2=}")
