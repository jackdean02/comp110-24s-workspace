"""EX04 - List Utility Functions."""

__author__ = "730385160"


def all(id1: list[int], id2: int) -> bool:
    """Return True or False if id2 matches all ints in id1."""
    list_counter: int = 0
    if len(id1) == 0:
        return False
    while list_counter <= len(id1) - 1:
        if id1[list_counter] == id2:
            list_counter += 1
        else:
            return False
    return True


def max(input: list[int]) -> int:
    """Returns largest int in list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    input_counter: int = 1
    max_int: int = input[0]
    while input_counter <= len(input) - 1:
        if input[input_counter] > max_int:
            max_int = input[input_counter]
        input_counter += 1
    return max_int


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns True or False if every element at every index in both lists match."""
    counter: int = 0
    if len(list1) == len(list2):
        while counter < len(list1):
            if list1[counter] == list2[counter]:
                counter += 1
            else:
                return False            
        return True
    else:
        return False


def extend(a_list: list[int], b_list: list[int]) -> None:
    """Appends the second list values to the first list."""
    counter: int = 0
    while counter <= len(b_list) - 1:
        a_list.append(b_list[counter])
        counter += 1