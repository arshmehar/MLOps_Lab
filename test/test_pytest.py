import pytest
from src import leetcode

def test_two_sum():
    assert leetcode.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert leetcode.two_sum([3, 3], 6) == [0, 1]
    assert leetcode.two_sum([-3, 4, 3, 90], 0) == [0, 2]
    assert leetcode.two_sum([1, 2, 3], 100) == []


def test_two_sum_sorted():
    assert leetcode.two_sum_sorted([1, 2, 3, 4, 5, 6], 0, 7) == [[1, 6], [2, 5], [3, 4]]
    assert leetcode.two_sum_sorted([1, 1, 2, 2, 3, 3], 0, 4) == [[1, 3], [2, 2]]
    assert leetcode.two_sum_sorted([1, 2, 3, 4], 1, 5) == [[2, 3]]
    assert leetcode.two_sum_sorted([1, 2], 0, 10) == []


def test_three_sum():
    assert leetcode.three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert leetcode.three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert leetcode.three_sum([0, 1, 1]) == []
    assert leetcode.three_sum([1, 2]) == []
    assert leetcode.three_sum([1, 2, 3, 4, 5], 9) == [[1, 3, 5], [2, 3, 4]]


def test_validate_nums():
    with pytest.raises(ValueError):
        leetcode.three_sum("123")
    with pytest.raises(ValueError):
        leetcode.two_sum([1, "a", 3], 4)
