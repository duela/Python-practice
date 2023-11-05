import pytest

from q02 import solve

TEST_CASES = [
    (0, {"0": 0, "1": 1, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}),
    (1, {"0": 0, "1": 1, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}),
]


@pytest.mark.parametrize("input,expected", TEST_CASES)
def test_solver(input, expected):
    assert solve(input) == expected
