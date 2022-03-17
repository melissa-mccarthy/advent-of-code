import pytest

from year_2015.day_3.main import count_houses_visited


@pytest.mark.parametrize(
    "directions, num_deliverers, expected_houses_visited",
    [
        (">", 1, 2),
        (">", 2, 2),
        ("^>v<", 1, 4),
        ("^>v<", 2, 3),
        ("^v", 1, 2),
        ("^v", 2, 3),
        ("^v^v^v^v^v", 1, 2),
        ("^v^v^v^v^v", 2, 11),
    ],
)
def test(directions: str, num_deliverers: int, expected_houses_visited: int):
    assert count_houses_visited(directions, num_deliverers) == expected_houses_visited
