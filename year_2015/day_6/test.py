from typing import List, Tuple

import pytest

from year_2015.day_6.main import (
    get_coordinates,
    update_brightness,
    update_grid,
    update_on_off,
)


@pytest.fixture(scope="function")
def ten_by_ten_off() -> List[List[bool]]:
    return [[False] * 10 for _ in range(10)]


@pytest.fixture(scope="function")
def ten_by_ten_on() -> List[List[bool]]:
    return [[True] * 10 for _ in range(10)]


@pytest.mark.parametrize(
    "command, expected",
    [
        ("turn on 0,0 through 9,9", ((0, 0), (9, 9))),
        ("toggle 0,0 through 9,0", ((0, 0), (9, 0))),
        ("turn off 4,4 through 5,5", ((4, 4), (5, 5))),
        ("toggle 0,0 through 999,999", ((0, 0), (999, 999))),
    ],
    ids=lambda x: str(x),
)
def test_get_coordinates(
    command: str, expected: Tuple[Tuple[int, int], Tuple[int, int]]
):
    assert get_coordinates(command) == expected


class TestOnOff:
    def test_all_on(
        self, ten_by_ten_off: List[List[bool]], ten_by_ten_on: List[List[bool]]
    ):
        command = "turn on 0,0 through 9,9"
        assert (
            update_grid(
                get_coordinates(command), update_on_off(command), ten_by_ten_off
            )
            == ten_by_ten_on
        )

    def test_all_off(
        self, ten_by_ten_off: List[List[bool]], ten_by_ten_on: List[List[bool]]
    ):
        command = "turn off 0,0 through 9,9"
        assert (
            update_grid(get_coordinates(command), update_on_off(command), ten_by_ten_on)
            == ten_by_ten_off
        )

    def test_all_toggle(
        self, ten_by_ten_off: List[List[bool]], ten_by_ten_on: List[List[bool]]
    ):
        command = "toggle 0,0 through 9,9"
        assert (
            update_grid(
                get_coordinates(command), update_on_off(command), ten_by_ten_off
            )
            == ten_by_ten_on
        )

    def test_toggle_first_row(self, ten_by_ten_off: List[List[bool]]):
        command = "toggle 0,0 through 9,0"
        assert update_grid(
            get_coordinates(command), update_on_off(command), ten_by_ten_off
        ) == ([[True] * 10] + [[False] * 10 for _ in range(9)])

    def test_turn_off_middle_square(self, ten_by_ten_on: List[List[bool]]):
        command = "turn off 4,4 through 5,5"
        assert update_grid(
            get_coordinates(command), update_on_off(command), ten_by_ten_on
        ) == (
            [[True] * 10 for _ in range(4)]
            + [
                [True, True, True, True, False, False, True, True, True, True]
                for _ in range(2)
            ]
            + [[True] * 10 for _ in range(4)]
        )


class TestBrightness:
    def test_turn_on_single(self):
        command = "turn on 0,0 through 0,0"
        updated_grid = update_grid(
            get_coordinates(command),
            update_brightness(command),
            [[0] * 10 for _ in range(10)],
        )
        assert sum([y for x in updated_grid for y in x]) == 1

    def test_toggle_all(self):
        command = "toggle 0,0 through 999,999"
        updated_grid = update_grid(
            get_coordinates(command),
            update_brightness(command),
            [[0] * 10000 for _ in range(10000)],
        )
        assert sum([y for x in updated_grid for y in x]) == 2000000
