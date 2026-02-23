from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(700, 700)
my_screen.bgcolor("black")

center_dash = Turtle()
center_dash.speed("fastest")
center_dash.penup()
center_dash.pencolor("white")
center_dash.pensize(8)
center_dash.setheading(270)
center_dash.setpos(0, 700)

for i in range(20):
    center_dash.pendown()
    center_dash.forward(30)
    center_dash.penup()
    center_dash.forward(30)

my_screen.exitonclick()



