from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

i: int = 0
while (i < 3):
        leo.forward(40)
        leo.left(120)
        i = i + 1
done()


star: Turtle = Turtle()
draw_star(star, -100.0, 175.0)
wheel: Turtle = Turtle()
draw_wheel(wheel, -50.0, -125.0, 50.0)
car: Turtle = Turtle()
window: Turtle = Turtle()
draw_window(window, 80.0, -100)

