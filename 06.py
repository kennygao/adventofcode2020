with open("input/06.txt") as f:
    groups = [
        [set(answers) for answers in group.split()] for group in f.read().split("\n\n")
    ]

part1 = sum(len(first.union(*rest)) for first, *rest in groups)
print(f"{part1=}")

part2 = sum(len(first.intersection(*rest)) for first, *rest in groups)
print(f"{part2=}")
