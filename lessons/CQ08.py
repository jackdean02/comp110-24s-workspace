"""CQ08 - Object Oriented Programming."""
from __future__ import annotations
__author__ = "730385160"

class Point:

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
        new_x = self.x * factor
        new_y = self.y * factor
        return Point(new_x, new_y)