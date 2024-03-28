"""EX 06 - Testing Dictionary Functions."""
__author__ = "730385160"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_first_use_case() -> None:
    """Test if invert function inverts the entire dictionary."""
    dict1: dict[str] = {"apple": "cat", "banana": "dog"}
    assert invert(dict1) == {"cat": "apple", "dog": "banana"}


def test_invert_second_use_case() -> None:
    """Test if the return dictionary value was previously the key."""
    dict1: dict[str] = {"apple": "cat", "banana": "dog"}
    ret_dict: dict = invert(dict1)
    assert ret_dict["cat"] == "apple"


def test_invert_edge_case() -> None:
    """Test edge case if invert function works with just a letter."""
    dict1: dict[str] = {"Jim": "Bo", "G": "Halpert"}
    ret_dict: dict = invert(dict1)
    assert ret_dict["Halpert"] == "G"


def test_favorite_color_first_use_case() -> None:
    """Test if favorite color is returned."""
    dict1: dict[str] = {"Joe": "Green", "Adam": "Blue", "Sammy": "Blue"}
    favorite_color(dict1)
    assert favorite_color(dict1) == "Blue"


def test_favorite_color_second_use_case() -> None:
    """Test functionality if only one color in the dictionary."""
    dict1: dict[str] = {"Will": "Brown"}
    assert favorite_color(dict1) == "Brown"


def test_favorite_color_edge_case() -> None:
    """Test functionality if there is a tie for favorite color."""
    dict1: dict[str] = {"Ben": "Blue", "Izzy": "Yellow", "Gerald": "Yellow", "AOB": "Blue"}
    assert favorite_color(dict1) == "Blue"


def test_count_first_use_case() -> None:
    """Test if count returns correct count."""
    list1: list[str] = ["cat", "rat", "hat", "cat"]
    ret_dict: dict[str, int] = count(list1)
    assert ret_dict["cat"] == 2


def test_count_second_use_case() -> None:
    """Test if count function with item only seen once in list."""
    list1: list[str] = ["frog"]
    ret_dict: dict[str, int] = count(list1)
    assert ret_dict["frog"] == 1


def test_count_edge_case() -> None:
    """Test if count function works if given empty list."""
    list1: list[str] = []
    assert count(list1) == {}


def test_alphabetizer_first_use_case() -> None:
    """Test functionality of alphabetizer function."""
    list1: list[str] = ["apple", "banana", "buddy"]
    assert alphabetizer(list1) == {"a": ["apple"], "b": ["banana", "buddy"]}


def test_alphabetizer_second_use_case() -> None:
    """Test functionality if the input list just has a letter and not a word."""
    list1: list[str] = ["A", "bread", "boring"]
    ret_dict: dict[str, str] = alphabetizer(list1)
    assert ret_dict["a"] == ["A"]


def test_alphabetizer_edge_case() -> None:
    """Tests alphabetizer function if input list is empty."""
    list1: list[str] = []
    assert alphabetizer(list1) == {}


def test_update_attendance_first_use_case() -> None:
    """Tests functionality of update_attendance if the day is already in attendance information."""
    dict1: dict = {"Monday": ["Matt", "Rishi"], "Tuesday": ["Kieran"]}
    day: str = "Tuesday"
    person: str = "Matt"
    update_attendance(dict1, day, person)
    assert dict1["Tuesday"] == ["Kieran", "Matt"]


def test_update_attendance_second_use_case() -> None:
    """Tests function if a new day is part of the updated information."""
    dict1: dict = {"Monday": ["Matt", "Rishi"], "Tuesday": ["Kieran"]}
    day: str = "Wednesday"
    person: str = "Rishi"
    update_attendance(dict1, day, person)
    assert dict1["Wednesday"] == ["Rishi"]


def test_update_attendance_edge_case() -> None:
    """Tests functionality with a new day and person included in the updated information."""
    dict1: dict = {"Monday": ["Matt", "Rishi"], "Tuesday": ["Kieran"]}
    day: str = "Friday"
    person: str = "Bo"
    update_attendance(dict1, day, person)
    assert dict1 == {"Monday": ["Matt", "Rishi"], "Tuesday": ["Kieran"], "Friday": ["Bo"]}