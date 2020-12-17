"""
Unit tests for challenge functions.

"""

import pytest

from ..challenges import (
    array_diff,
    binary_array_to_number,
    is_array_squared,
    first_non_repeating_letter,
    find_uneven_occurrences,
    count_vowels,
)


@pytest.mark.parametrize(
    "array_a, array_b, result",
    [
        ([1, 2, 2, 2, 3], [2], [1, 3]),
        ([2], [1, 2, 2, 2, 3], []),
        (["a", 7.8, 0, False], [1, 7.8, True, False, True], ["a"]),
        (["abc", "def", "abb"], ["def", 789, "abc"], ["abb"]),
    ],
)
def test_array_diff(array_a, array_b, result):
    assert array_diff(array_a, array_b) == result


@pytest.mark.parametrize(
    "array, result", [([1, 1, 1, 1], 15), ([1, 0, 0, 1, 0, 1], 37), ([1, 0, 0], 4), ([0, 1, 0, 1, 1, 1, 0], 46)]
)
def test_binary_array_to_number(array, result):
    assert binary_array_to_number(array) == result


@pytest.mark.parametrize(
    "array_a, array_b, result",
    [
        ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], True),
        ([3, -7, 9], [9, 49, 81], True),
        ([3, -7, 9], [9, 49, -81], False),
        ([-11, -4, -2, 0, 2], [121, 16, 4, 0, 4], True),
        ([-11, -4, -2, 0, 2], [0, 4, 16, 4, 121], False),
    ],
)
def test_is_array_squared(array_a, array_b, result):
    assert is_array_squared(array_a, array_b) == result


@pytest.mark.parametrize(
    "string, result", [("AabbDNneccddffgg", "e"), ("FegoSowfgWQe", "s"), ("KaokiQowSza", "i"), ("aABbcCDdEefFGgg", "")]
)
def test_first_non_repeating_letter(string, result):
    assert first_non_repeating_letter(string) == result


@pytest.mark.parametrize(
    "array, result",
    [
        ([5, 4, 3, 2, 1, 2, 3, 4, 5], 1),
        ([5, 4, 3, 2, 1, 2, 3, 4, 5, 1], None),
        ([-1, 2, 4, 2, 4], -1),
        ([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5], 5),
    ],
)
def test_find_uneven_occurrences(array, result):
    assert find_uneven_occurrences(array) == result


@pytest.mark.parametrize(
    "string, result", [("This is a sentence", 6), ("Soft Kitty", 2), ("abcdefghij", 3), ("https://www", 0)]
)
def test_count_vowels(string, result):
    assert count_vowels(string) == result
