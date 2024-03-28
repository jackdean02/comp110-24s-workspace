"""Summing the elements of a list using different loops."""

__author__ = "730385160"


def w_sum(vals: list[float]) -> float:
    """Returns the sum of all elements."""
    counter: int = 0
    total: float = 0
    while counter < len(vals):
        total += vals[counter]
        counter += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Returns the sum of all elements."""
    total: float = 0
    for elem in vals:
        total += elem
    return total


def f_range_sum(vals: list[float]) -> float:
    """Returns the sum of all elements."""
    total: float = 0
    for idx in range(0, len(vals)):
        total += vals[idx]
    return total