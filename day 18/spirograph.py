from turtle import Turtle, Screen
import random

timmy= Turtle()

my_screen= Screen()


# timmy.pensize(2)
timmy.speed("fastest")
num=5
for i in range(144):
    colours= ["orange", "blue", "black", "yellow", "purple", "red", "green", "grey"]
    timmy.color(random.choice(colours))
    timmy.circle(150)
    timmy.setheading(num)
    num+=5

my_screen.exitonclick