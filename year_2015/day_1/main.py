from collections import Counter


def calculate_final_floor(directions: str) -> int:
    counter = Counter(directions)
    return counter.get("(", 0) - counter.get(")", 0)


def calculate_moves_to_floor(directions: str, floor: int) -> int:
    current_floor = 0
    for move_count, direction in enumerate(directions, 1):
        current_floor += 1 if direction == "(" else -1
        if current_floor == floor:
            return move_count


if __name__ == "__main__":
    with open("./input.txt", "r") as f:
        puzzle_input = f.readlines()[0]

    print(f"Final Floor: {calculate_final_floor(puzzle_input)}")
    print(f"Number of Moves to Basement: {calculate_moves_to_floor(puzzle_input, -1)}")
