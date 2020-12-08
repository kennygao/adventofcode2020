with open("input/08.txt") as f:
    lines = [line.rstrip("\n") for line in f]


def parse(line):
    operation, argument, *_ = line.split()
    return operation, int(argument)


code = [parse(line) for line in lines]


def run(program):
    seen = set()
    pc = 0
    accumulator = 0
    while pc not in seen:
        if pc == len(program):
            return 0, accumulator
        seen.add(pc)
        operation, argument = program[pc]
        if operation == "acc":
            accumulator += argument
            pc += 1
        if operation == "jmp":
            pc += argument
        if operation == "nop":
            pc += 1
    return 1, accumulator


_, part1 = run(code)
print(f"{part1=}")


def uncorrupt(program):
    swap = {"jmp": "nop", "nop": "jmp"}
    for i, (operation, argument) in enumerate(program):
        if operation in swap:
            loop, accumulator = run(
                [*program[:i], (swap[operation], argument), *program[i + 1 :]]
            )
            if not loop:
                return accumulator


part2 = uncorrupt(code)
print(f"{part2=}")
