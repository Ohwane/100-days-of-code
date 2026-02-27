import turtle
from turtle import Turtle
import pandas as pd

screen = turtle.Screen()
# screen.setup(700, 700)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



states_data = pd.read_csv("50_states.csv")


quiz_on = True
counter = 0
while quiz_on:

    answer = screen.textinput(title="quiz box", prompt="Enter the name of the state:")
    state = states_data[states_data.state == answer].state
    x_cor = int(states_data[states_data.state == answer].x)
    y_cor = int(states_data[states_data.state == answer].y)
    name_turtle = Turtle()
    name_turtle.hideturtle()
    name_turtle.penup()
    name_turtle.color("black")
    name_turtle.goto(x_cor, y_cor)
    name_turtle.write(f"{answer}", font=("Arial", 12, "normal"))

    counter += 1
    print(counter)
    if counter == 50:
        quiz_on = False

screen.exitonclick()
