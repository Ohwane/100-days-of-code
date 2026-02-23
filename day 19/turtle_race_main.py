from turtle import Turtle, Screen
import random

my_screen = Screen()

my_screen.setup(height=800, width=1000)
colours = ["red", "blue", "green", "yellow", "purple", "orange"]

race_turtles = []

my_bet = my_screen.textinput(title="Turtle Race", prompt="Place your bet of which turtle will win")

line = Turtle()
line.penup()
line.setpos(x=350, y=400)
line.setheading(270)
line.pensize(10)

for i in range(20):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

ypositions = [-250, -150, 0, 150, 250, 350]

movements = [30, 20, 40, 50, 33, 44, 60, 56, 15, 25, 29, 35, 49]

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[i])
    new_turtle.setposition(x=-350, y=ypositions[i])
    race_turtles.append(new_turtle)

race_on = True
while race_on:
    for i in race_turtles:
        i.forward(random.choice(movements))
        if i.pos() >= (350,None):
            race_on = False
            if my_bet == i.fillcolor():
                race_on = False
                my_screen.textinput(title="Match Result", prompt="Congratulations! Your Turtle won!")
                print(i.color())
            else:
                race_on = False
                my_screen.textinput(title="Match Result", prompt="Whoops! " + i.fillcolor() + " won. Better luck next "
                                                                                              "time!")
                print(i.color())

my_screen.exitonclick()
