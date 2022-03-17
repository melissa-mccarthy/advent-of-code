def count_houses_visited(directions: str, num_deliverers: int) -> int:
    houses = [[(0, 0)] * num_deliverers]
    for i, direction in enumerate(directions):
        last_coordinates = houses[-1].copy()
        deliverer = i % num_deliverers
        x, y = last_coordinates[deliverer]
        if direction in ["^", "v"]:
            y += 1 if direction == "^" else -1
        else:
            x += 1 if direction == ">" else -1
        last_coordinates[deliverer] = (x, y)
        houses.append(last_coordinates)
    return len(set(house for move in houses for house in move))


if __name__ == "__main__":
    with open("year_2015/day_3/input.txt", "r") as f:
        puzzle_input = f.readlines()[0]
    year_1_houses_visited = count_houses_visited(puzzle_input, 1)
    print(f"{year_1_houses_visited} houses visited first year")
    year_2_houses_visited = count_houses_visited(puzzle_input, 2)
    print(f"{year_2_houses_visited} houses visited second year")
