with open("input/05.txt") as f:
    lines = [line.rstrip("\n") for line in f]

cipher = str.maketrans({"F": "0", "B": "1", "L": "0", "R": "1"})


def parse(seat):
    return int(seat.translate(cipher), 2)


seats = list(map(parse, lines))

part1 = max(seats)
print(f"{part1=}")


def rangesum(start, stop):
    return (stop * (stop - 1) - start * (start - 1)) // 2


part2 = rangesum(min(seats), max(seats) + 1) - sum(seats)
print(f"{part2=}")
