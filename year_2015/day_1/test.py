from typing import List

import pytest

from year_2015.day_1.main import calculate_final_floor, calculate_moves_to_floor


@pytest.mark.parametrize(
    "directions, final_floor",
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
    ],
)
def test_calculate_final_floor(directions: str, final_floor: int):
    assert calculate_final_floor(directions) == final_floor


@pytest.mark.parametrize(
    "directions, floors",
    [
        ("(())", [1, 2, 1, 0]),
        ("()()", [1, 0, 1, 0]),
        ("(((", [1, 2, 3]),
        ("(()(()(", [1, 2, 1, 2, 3, 2, 3]),
        ("))(((((", [-1, -2, -1, 0, 1, 2, 3]),
        ("())", [1, 0, -1]),
        ("))(", [-1, -2, -1]),
        (")))", [-1, -2, -3]),
        (")())())", [-1, 0, -1, -2, -1, -2, -3]),
    ],
    ids=lambda x: str(x),
)
def test_calculate_moves_to_floor(directions: str, floors: List[int]):
    for current_position in set(floors):
        assert (
            calculate_moves_to_floor(directions, current_position)
            == floors.index(current_position) + 1
        )
