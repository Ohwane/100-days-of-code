from turtle import Turtle
import time


class CenterDash(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.showturtle()
        self.penup()
        self.pencolor("white")
        self.pensize(8)
        self.setheading(270)
        self.setpos(0, 700)
        for i in range(20):
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)



