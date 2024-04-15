"""CQ08 - Object Oriented Programming."""
from __future__ import annotations
__author__ = "730385160"


class Point:
    """New class created called Point with two attributes."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Assigns values for x and y."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Updates x and y and scales them by the above factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Returns new Point with x and y attributes scaled to a factor."""
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled
    
    def __str__(self):
        """Print prettier version of our point."""
        return f"({self.x}, {self.y})"
    
    def __mul__(self, factor: float) -> Point:
        """Returns new Point with x and y attributes scaled to a factor."""
        scaled: Point = Point(self.x * factor, self.y * factor)
        return scaled

    def __getitem__(self, index: int) -> float:
        """Overloading subscription notation."""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError


a: Point = Point(1.0, 2.0)
b: Point = a * 3.0
print(b(1)) # y-coord