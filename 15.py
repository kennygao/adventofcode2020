from common import lines


def play(start, turns):
    heard = {}
    last = -1
    for i in range(turns):
        if i < len(start):
            say = start[i]
        elif last in heard:
            say = i - 1 - heard[last]
        else:
            say = 0
        heard[last] = i - 1
        last = say
    return last


start = [int(n) for n in lines("15")[0].split(",")]

part1 = play(start, 2020)
print(f"{part1=}")

part2 = play(start, 30000000)
print(f"{part2=}")
