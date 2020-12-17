"""
A set of challenge functions.

"""
from collections import Counter
from typing import List, Union


def array_diff(array_a: list, array_b: list) -> list:
    """Get those elements from the first list which are not in the second one."""
    return list(set(array_a) - set(array_b))


def binary_array_to_number(array: List[int]) -> int:
    """Convert a list of bits into an integer."""
    return int("".join(map(str, array)), base=2)


def is_array_squared(array_a: List[int], array_b: List[int]) -> bool:
    """Check whether the second array is equal to the first squared array."""
    return [i ** 2 for i in array_a] == array_b


def first_non_repeating_letter(string: str) -> str:
    """Get the first non repeating letter from the string."""
    try:
        return [i[0] for i in Counter(string.lower()).items() if i[1] == 1][0]
    except IndexError:
        return ""


def find_uneven_occurrences(array: List[int]) -> Union[int, None]:
    """Find the last one integer which occurs an odd number of times."""
    try:
        return [i[0] for i in Counter(array).items() if i[1] % 2 == 1][-1]
    except IndexError:
        return None


def count_vowels(string: str) -> int:
    """Count and return a number of vowels."""
    return sum([i[1] for i in Counter(string).items() if i[0] in ("a", "e", "i", "o", "u")])
