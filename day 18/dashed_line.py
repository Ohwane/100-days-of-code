from turtle import Turtle, Screen

timmy= Turtle()
timmy.color("green")
timmy.shape("turtle")
my_screen= Screen()

for i in range(50):
    timmy.forward(5)
    timmy.penup()
    timmy.forward(5)
    timmy.pendown()

my_screen.canvwidth(500)
my_screen.canvheight(500)
my_screen.exitonclick()