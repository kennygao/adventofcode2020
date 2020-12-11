def lines(day):
    with open(f"input/{day}.txt") as f:
        return [line.rstrip("\n") for line in f]


seats = [list(line) for line in lines("11")]
m, n = len(seats), len(seats[0])


def fixed_point(neighbor_function, crowd_factor, grid):
    def tick():
        def tick_cell(r, c):
            if grid[r][c] == ".":
                return "."
            elif grid[r][c] == "L":
                return "#" if neighbor_function(grid, r, c) == 0 else "L"
            elif grid[r][c] == "#":
                return "L" if neighbor_function(grid, r, c) >= crowd_factor else "#"

        return [[tick_cell(r, c) for c in range(n)] for r in range(m)]

    while grid != (next_grid := tick()):
        grid = next_grid
    return grid


directions = {(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)}


def neighbors1(grid, r, c):
    return sum(
        grid[r + dr][c + dc] == "#"
        for dr, dc in directions
        if 0 <= r + dr < m and 0 <= c + dc < n
    )


part1 = sum(row.count("#") for row in fixed_point(neighbors1, 4, seats))
print(f"{part1=}")


def neighbors2(grid, r, c):
    def look(dr, dc):
        cr, cc = r, c
        while 0 <= (cr := cr + dr) < m and 0 <= (cc := cc + dc) < n:
            if grid[cr][cc] == "#":
                return True
            elif grid[cr][cc] == "L":
                return False

        return False

    return sum(look(dr, dc) for dr, dc in directions)


part2 = sum(row.count("#") for row in fixed_point(neighbors2, 5, seats))
print(f"{part2=}")
