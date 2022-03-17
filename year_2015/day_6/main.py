import re
from copy import deepcopy
from typing import Callable, List, Tuple, Union

RE_COORDINATES = re.compile(r"([0-9]+),([0-9]+)")


def get_coordinates(command: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    start, end = [(int(x), int(y)) for x, y in RE_COORDINATES.findall(command)]
    return start, end


def update_on_off(command: str) -> Callable[[bool], bool]:
    if command.startswith("toggle"):
        return lambda current_value: not current_value
    if command.startswith("turn on"):
        return lambda _: True
    if command.startswith("turn off"):
        return lambda _: False
    raise ValueError(f"Unknown command: {command}")


def update_brightness(command: str) -> Callable[[int], int]:
    if command.startswith("toggle"):
        return lambda current_value: current_value + 2
    if command.startswith("turn on"):
        return lambda current_value: current_value + 1
    if command.startswith("turn off"):
        return lambda current_value: (current_value - 1) if current_value > 0 else 0
    raise ValueError(f"Unknown command: {command}")


def update_grid(
    coordinates: Tuple[Tuple[int, int], Tuple[int, int]],
    change_fn: Callable,
    current_grid: List[List[Union[bool, int]]],
) -> List[List[Union[bool, int]]]:
    updated_grid = deepcopy(current_grid)
    for x in range(coordinates[0][0], coordinates[1][0] + 1):
        for y in range(coordinates[0][1], coordinates[1][1] + 1):
            updated_grid[y][x] = change_fn(updated_grid[y][x])

    return updated_grid


if __name__ == "__main__":
    on_off_current = [[False] * 1000 for _ in range(1000)]
    brightness_current = [[0] * 1000 for _ in range(1000)]
    with open("year_2015/day_6/input.txt", "r") as f:
        for line in f.readlines():
            on_off_current = update_grid(
                get_coordinates(line), update_on_off(line), on_off_current
            )
            brightness_current = update_grid(
                get_coordinates(line), update_brightness(line), brightness_current
            )

    lit = len([y for x in on_off_current for y in x if y is True])
    print(f"{lit} lights are lit")

    total_brightness = sum([y for x in brightness_current for y in x])
    print(f"{total_brightness} total brightness")
