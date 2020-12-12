from common import lines

instructions = [(line[0], int(line[1:])) for line in lines("12")]

directions = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}


def simulate(commands, mode, start_position, start_direction):
    x, y = start_position
    dx, dy = start_direction
    for action, value in commands:
        if action in directions:
            vx, vy = directions[action]
            if mode == 1:
                x, y = x + vx * value, y + vy * value
            if mode == 2:
                dx, dy = dx + vx * value, dy + vy * value
        elif action == "L":
            for _ in range(value // 90):
                dx, dy = -dy, dx
        elif action == "R":
            for _ in range(value // 90):
                dx, dy = dy, -dx
        elif action == "F":
            x, y = x + dx * value, y + dy * value
    return abs(x) + abs(y)


part1 = simulate(instructions, mode=1, start_position=(0, 0), start_direction=(1, 0))
print(f"{part1=}")


part2 = simulate(instructions, mode=2, start_position=(0, 0), start_direction=(10, 1))
print(f"{part2=}")
