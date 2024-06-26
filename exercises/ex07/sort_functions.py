"""Functions that implement sorting algorithms."""

__author__ = "730385160"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm."""
    for idx in range(1, len(x)):
        value = x[idx]
        y = idx - 1
        while y >= 0 and value < x[y]:
            x[y + 1] = x[y]
            y -= 1
        x[y + 1] = value
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm, repeatedly finds the minimum and swaps it."""
    for idx in range(len(x)):
        min_idx = idx
        for y in range(min_idx + 1, len(x)):
            if x[y] < x[min_idx]:
                min_idx = y
        if min_idx != idx:
            temp_int = x[idx]
            x[idx] = x[min_idx]
            x[min_idx] = temp_int
    return None