"""EX08: Nightime Drive."""

__author__ = "730385160"
from turtle import Turtle, Screen, colormode, done
colormode(255)

screen = Screen()
screen.bgcolor(153, 50, 204)


def main() -> None:
    """Entry point for my scene."""
    star1: Turtle = Turtle()
    star2: Turtle = Turtle()
    wheel1: Turtle = Turtle()
    wheel2: Turtle = Turtle()
    car: Turtle = Turtle()
    window: Turtle = Turtle()
    heading: Turtle = Turtle()
    draw_star(star1, -100.0, 175.0)
    draw_star(star2, 100.0, 150.0)
    draw_wheel(wheel1, -50.0, -210.0, 50.0)
    draw_wheel(wheel2, 100, -210.0, 50.0)
    draw_car(car, -100.0, -130.0)
    draw_window(window, 80.0, -65.0)
    pic_title(heading, -10.0, 230.0)
    done()


def draw_star(star: Turtle, x: float, y: float) -> None:
    """Draw a star with marker color yellow at given x and y, will be called twice in picture."""
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.color("yellow")
    i: int = 0
    while i < 5:
        star.forward(100)
        star.right(144)
        i += 1
    star.pendown()


def draw_wheel(wheel: Turtle, x: float, y: float, radius: float) -> None:
    """Draw circle for wheel of car at x and y, used recursion to include smaller circles within."""
    wheel.penup()
    wheel.goto(x, y)
    wheel.pendown()
    wheel.circle(radius, 360)
    wheel.speed(0)
    if radius < 5:
        return
    draw_wheel(wheel, x, y, 0.99 * radius)


def draw_car(car: Turtle, x: float, y: float) -> None:
    """Draw a rectangle for the car at the given coordinates."""
    car.fillcolor("green")
    car.begin_fill()
    car.penup()
    car.goto(x, y)
    car.pendown()
    i: int = 0
    while i < 2:
        car.forward(250)
        car.left(90)
        car.forward(125)
        car.left(90)
        i += 1
    car.pendown()
    car.end_fill()


def draw_window(window: Turtle, x: float, y: float) -> None:
    """Draws white filled window at x and y, breaking up the complex function of drawing whole car at once."""
    window.fillcolor("white")
    window.begin_fill()
    window.penup()
    window.goto(x, y)
    window.pendown()
    i: int = 0
    while i < 4:
        window.forward(50)
        window.left(90)
        i += 1
    window.pendown()
    window.end_fill()


def pic_title(heading: Turtle, x: float, y: float) -> None:
    """Draws the title of the picture at x and y, uses new function to go above and beyond."""
    heading.penup()
    heading.goto(x, y)
    heading.write("Nightime Drive", False, align="center", font=("Arial", 18, "normal"))


if __name__ == "__main__":
    main()