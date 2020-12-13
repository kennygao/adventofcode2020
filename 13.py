from functools import reduce

from common import lines

departure, schedule = lines("13")
buses = [
    (-time % int(bus), int(bus))
    for time, bus in enumerate(schedule.split(","))
    if bus != "x"
]

delay, bus = min((-int(departure) % bus, bus) for _, bus in buses)
part1 = delay * bus
print(f"{part1=}")


def crt_sieve(c1, c2):
    a1, n1 = c1
    a2, n2 = c2
    while a1 % n2 != a2:
        a1 += n1
    return a1, n1 * n2


part2, _ = reduce(crt_sieve, buses)
print(f"{part2=}")
