"""Challenge Question 7: Recursion."""
__author__ = "730385160"


def f(n: int, k: int) -> int:
    """Function we are doing recursion with."""
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)