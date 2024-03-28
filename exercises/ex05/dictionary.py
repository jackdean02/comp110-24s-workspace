"""EX05 - Dictionary Functions."""

__author__ = "730385160"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Returns dictionary that inverts the keys and values."""
    invert_dict: dict[str, str] = {}
    for key in dict1:
        value: str = dict1[key]
        if value in invert_dict:
            raise KeyError("Duplicate values when inverting dictionary.")
        invert_dict[value] = key
    return invert_dict


def favorite_color(dict1: dict[str, str]) -> str:
    """Returns most common color from dictionary."""
    color_count: dict[str, int] = {}
    for x in dict1:
        color: str = dict1[x]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    most_pop: str = ""
    max: int = 0
    for color in color_count:
        if color_count[color] > max:
            most_pop = color
            max = color_count[color]
    return most_pop


def count(list1: list[str]) -> dict[str, int]:
    """Returns dict with a count of how many times keys appear in the list."""
    dict1: dict[str, int] = {}
    for x in list1:
        if x in dict1:
            dict1[x] += 1
        else:
            dict1[x] = 1
    return dict1


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Returns dictionary of the letters and words that belong to that letter."""
    dict1: dict[str, list[str]] = {}
    for elem in list1:
        letter: str = elem[0].lower()
        if letter not in dict1:
            dict1[letter] = []
        dict1[letter].append(elem)
    return dict1


def update_attendance(dict1: dict[str, list[str]], day: str, person: str) -> None:
    """Returns updated dictionary with correct attendance."""
    if day in dict1:
        dict1[day].append(person)
    else:
        dict1[day] = [person]