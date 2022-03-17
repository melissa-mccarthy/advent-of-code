import pytest

from year_2015.day_5.main import new_rules_is_nice, old_rules_is_nice


@pytest.mark.parametrize(
    "s, is_nice",
    [
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", False),
        ("haegwjzuvuyypxyu", False),
        ("dvszwmarrgswjxmb", False),
    ],
)
def test_old_rules(s: str, is_nice: bool):
    assert old_rules_is_nice(s) == is_nice


@pytest.mark.parametrize(
    "s, is_nice",
    [
        ("qjhvhtzxzqqjkmpb", True),
        ("xxyxx", True),
        ("uurcxstgmygtbstg", False),
        ("ieodomkazucvgmuy", False),
    ],
)
def test_new_rules(s: str, is_nice: bool):
    assert new_rules_is_nice(s) == is_nice
