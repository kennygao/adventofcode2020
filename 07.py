from collections import defaultdict

with open("input/07.txt") as f:
    lines = [line.rstrip("\n") for line in f]


def parse(line):
    outer, contents = line.split(" bags contain ")
    return outer, {
        " ".join(tokens[1:3]): int(tokens[0])
        for inner in contents.split(", ")
        if (tokens := inner.split())[0] != "no"
    }


bag_contents = dict(map(parse, lines))


def invert(graph):
    # doesn't preserve weights
    inverted = defaultdict(set)
    for outer, contents in graph.items():
        for inner in contents.keys():
            inverted[inner].add(outer)
    return inverted


def reachable_from(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited


part1 = len(reachable_from(invert(bag_contents), "shiny gold")) - 1
print(f"{part1=}")


def bags_inside(outer):
    return sum(
        count + count * bags_inside(inner)
        for inner, count in bag_contents[outer].items()
    )


part2 = bags_inside("shiny gold")
print(f"{part2=}")
