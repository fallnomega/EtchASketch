# EtchASketch
import turtle as t


def move_forward():
    sketcher.forward(50)


def move_backwards():
    sketcher.left(180)
    sketcher.back(50)


def reset_screen():
    sketcher.reset()


def turn_right():
    new_heading = sketcher.heading() - 10
    sketcher.setheading(new_heading)


def turn_left():
    new_heading = sketcher.heading() + 10
    sketcher.setheading(new_heading)


sketcher = t.Turtle()
screen = t.Screen()
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='c', fun=reset_screen)

screen.exitonclick()
