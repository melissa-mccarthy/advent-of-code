import pytest

from year_2015.day_4.main import get_value


@pytest.mark.parametrize(
    "secret_key, starts_with, expected_value",
    [("abcdef", "00000", 609043), ("pqrstuv", "00000", 1048970)],
)
def test(secret_key: str, starts_with: str, expected_value: int):
    assert get_value(secret_key, starts_with) == expected_value
