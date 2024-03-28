"""Functions that either mutate a list or don't."""

def remove_first(input: list[str]) -> None:
    """Removes first element of input_list. Mutating!"""
    input.pop(0)

def get_first(input: list[str]) -> str:
    """Return first element of input list without mutating."""
    return input[0]

def get_and_remove_first(input: list[str]) -> str:
    """Return first element AND remove it."""
    elem: str = input[0]
    input.pop(0)
    return elem