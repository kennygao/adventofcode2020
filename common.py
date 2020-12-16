def lines(day):
    with open(f"input/{day}.txt") as f:
        return [line.rstrip("\n") for line in f]


def line_groups(day):
    with open(f"input/{day}.txt") as f:
        return [group.rstrip("\n").split("\n") for group in f.read().split("\n\n")]
