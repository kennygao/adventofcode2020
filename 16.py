import math
import operator
from itertools import chain

from common import line_groups


def parse_constraints(lines):
    return {
        field: [tuple(map(int, r.split("-"))) for r in ranges.split(" or ")]
        for field, ranges in (line.split(": ") for line in lines)
    }


def parse_ticket(line):
    return [int(v) for v in line.split(",")]


def error(ticket):
    errors = [
        v
        for v in ticket
        if not any(
            lo <= v <= hi for ranges in constraints.values() for lo, hi in ranges
        )
    ]

    return sum(errors), len(errors)


constraints_lines, your_ticket_lines, nearby_tickets_lines = line_groups("16")

constraints = parse_constraints(constraints_lines)
your_ticket = parse_ticket(your_ticket_lines[1])
nearby_tickets = [parse_ticket(line) for line in nearby_tickets_lines[1:]]

part1 = sum(error(t)[0] for t in nearby_tickets)
print(f"{part1=}")

valid_tickets = [t for t in nearby_tickets if not error(t)[1]]

possible_assignments = {
    field: {
        i
        for i in range(len(your_ticket))
        if all(any(lo <= t[i] <= hi for lo, hi in ranges) for t in valid_tickets)
    }
    for field, ranges in constraints.items()
}

# sets are sortable by < (issubset)!
fields, possible_columns = zip(
    *sorted(possible_assignments.items(), key=operator.itemgetter(1))
)

assigned_columns = (
    (a - b).pop() for a, b in zip(possible_columns, chain([set()], possible_columns))
)

assignments = dict(zip(fields, assigned_columns))

part2 = math.prod(
    your_ticket[column]
    for field, column in assignments.items()
    if field.startswith("departure")
)
print(f"{part2=}")
