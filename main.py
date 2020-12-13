from turtle import Turtle, Screen, colormode
import random

my_turtle = Turtle()
my_turtle.shape("arrow")
my_turtle.pensize(3)
my_turtle.speed(0)
my_color_mode = colormode(255)
direction = [0, 90, 180, 270]


def color_maker():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


for c in range(300):
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(direction))
    my_turtle.pencolor(color_maker())


my_screen = Screen()
my_screen.exitonclick()

