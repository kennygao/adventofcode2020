from itertools import combinations

with open("input/09.txt") as f:
    numbers = [int(line.rstrip("\n")) for line in f]


def valid(i):
    return i < 25 or any(
        sum(c) == numbers[i] for c in combinations(numbers[i - 25 : i], 2)
    )


part1 = next(n for i, n in enumerate(numbers) if not valid(i))
print(f"{part1=}")


def contiguous_span(span_sum):
    lo, hi, total = 0, 0, 0
    while total != span_sum:
        if total < span_sum:
            total += numbers[hi]
            hi += 1
        if total > span_sum:
            total -= numbers[lo]
            lo += 1
    return numbers[lo:hi]


span = contiguous_span(part1)
part2 = min(span) + max(span)
print(f"{part2=}")
