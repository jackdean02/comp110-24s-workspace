"""Mutating functions."""
__author__ = "730385160"


def manual_append(word1: list[int], word2: int) -> None:
    """This function appends word2 to the word1 list."""
    word1.append(word2)


def double(a: list[int]) -> None:
    """Function will multiply every parameter in list by 2."""
    list_counter: int = 0
    while list_counter <= (len(a) - 1):
        a[list_counter] = a[list_counter] * 2
        list_counter += 1