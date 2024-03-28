"""Splitting a dictionary into two lists."""

__author__ = "730385160"


def get_keys(dict1: dict[str, int]) -> list[str]:
    """Returns list of all keys in dictionary."""
    list1: list[str] = []
    for key in dict1:
        list1.append(key)
    return list1


def get_values(dict1: dict[str, int]) -> list[int]:
    """Returns list of all values in dictionary."""
    list1: list[int] = []
    for key in dict1:
        list1.append(dict1[key])
    return list1