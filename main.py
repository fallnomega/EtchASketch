import turtle as t
#
# timmy = t.Turtle()
# screen = t.Screen()
#
# def move_forward():
#     timmy.forward(10)
#
# screen.listen()
# screen.onkey(key="space",fun=move_forward)
#
# screen.exitonclick()
#


# EtchASketch

def move_forward():
    sketcher.forward(50)
def turn_left():
    sketcher.left(90)
def turn_right():
    sketcher.right(90)
def move_backwards():
    sketcher.back(50)

def reset_screen():
    sketcher.reset()

sketcher = t.Turtle()
screen = t.Screen()
screen.listen()
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backwards)
screen.onkey(key='d',fun=turn_right)
screen.onkey(key='a',fun=turn_left)
screen.onkey(key='c',fun=reset_screen)









screen.exitonclick()





