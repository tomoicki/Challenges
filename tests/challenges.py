"""
Unit tests for challenge functions.

"""

import pytest

from ..challenges import (
    arabic_to_roman,
    array_diff,
    binary_array_to_number,
    bracket_validator,
    count_vowels,
    encrypt_message,
    find_substrings,
    find_uneven_occurrences,
    first_non_repeating_letter,
    is_array_squared,
    is_square,
    is_triangle,
    move_zeros,
    string_middle,
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


@pytest.mark.parametrize(
    "string, result",
    [("middle", "dd"), ("begin", "g"), ("end", "n"), ("foo bar", " "), ("", ""), ("AZ", "AZ"), ("A", "A")],
)
def test_string_middle(string, result):
    assert string_middle(string) == result


@pytest.mark.parametrize(
    "array_a, array_b, result",
    [
        (["dog", "she", "shell"], ["shelly", "watchdog"], ["dog", "she", "shell"]),
        (["xyz", "X", "Foo"], ["Arch-X"], ["X"]),
        (["abc", "def"], ["xyz"], []),
        (["Foo", "Bar", "Baz"], ["Foo", "Bar", "Baz"], ["Foo", "Bar", "Baz"]),
    ],
)
def test_find_substrings(array_a, array_b, result):
    assert find_substrings(array_a, array_b) == result


@pytest.mark.parametrize(
    "number, result",
    [(4, True), (81, True), (16, True), (11, False), (1, True), (0, True), (100, True), (21.3, False), (99.9, False)],
)
def test_is_square(number, result):
    assert is_square(number) == result


@pytest.mark.parametrize(
    "sides, result",
    [((3, 5, 8.0), False), ((4, 2.1, 3), True), ((1.0, 1, 1), True), ((10, 4.7, 5), False), ((0.1, 2.2, 1.4), False)],
)
def test_is_triangle(sides, result):
    assert is_triangle(sides) == result


@pytest.mark.parametrize(
    "array, result",
    [
        ([False, 1, 0, 1, 2, 0, 1, 3, "a"], [False, 1, 1, 2, 1, 3, "a", 0, 0]),
        ([0, 0, 0, 1, 0], [1, 0, 0, 0, 0]),
        ([0, -1, True, False, 2 + 8j, -4.9], [-1, True, False, 2 + 8j, -4.9, 0]),
        ([0], [0]),
        ([3.1, -9.3, 0.0, False, 1, 3, (2, 3.7)], [3.1, -9.3, 0.0, False, 1, 3, (2, 3.7)]),
    ],
)
def test_move_zeros(array, result):
    assert move_zeros(array) == result


@pytest.mark.parametrize(
    "string, result",
    [
        ("(())((()())())", True),
        ("This is a (bracket)", True),
        ("<(...)(>", False),
        ("<(...)((>", False),
        ("a)b(c)d", False),
        ("", True),
        (")))(((", False),
        ("(This) (is) )a( (bracket)", False),
        ("def function(arg1, arg2):", True),
        ("result = function((1, 2, 3), (True):", False),
    ],
)
def test_bracket_validator(string, result):
    assert bracket_validator(string) == result


@pytest.mark.parametrize(
    "string, result",
    [
        ("Foo Baz Bar", ".*****.***."),
        ("Earth Moon Sun", ".....*.****..*"),
        ("machine learning", ".*..***..**.***."),
        ("data science", ".*.*..*.*.**"),
        ("", ""),
    ],
)
def test_encrypt_message(string, result):
    assert encrypt_message(string) == result


@pytest.mark.parametrize(
    "number, result",
    [(1999, "MCMXCIX"), (2000, "MM"), (79, "LXXIX"), (83, "LXXXIII"), (949, "CMXLIX"), (3967, "MMMCMLXVII")],
)
def test_arabic_to_roman(number, result):
    assert arabic_to_roman(number) == result
