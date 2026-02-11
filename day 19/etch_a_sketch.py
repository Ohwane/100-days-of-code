from turtle import Turtle, Screen

tim = Turtle()

my_screen = Screen()

# def go_up():
#     tim.setheading(90)
#     tim.forward(30)
#
# def go_left():
#     tim.setheading(180)
#     tim.forward(30)
#
# def go_down():
#     tim.setheading(270)
#     tim.forward(30)
#
# def go_right():
#     tim.setheading(0)
#     tim.forward(30)

def go_up():
    tim.forward(20)

def go_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def go_down():
    tim.backward(20)

def go_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

my_screen.listen()
my_screen.onkey(key="w", fun=go_up)
my_screen.onkey(key="a", fun=go_left)
my_screen.onkey(key="s", fun=go_down)
my_screen.onkey(key="d", fun=go_right)

my_screen.exitonclick()
