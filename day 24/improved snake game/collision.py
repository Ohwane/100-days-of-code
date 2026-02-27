# from snake import Snake
from turtle import Turtle

class Collide(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 0)
        self.walls()
        self.snake_tail()

    def walls(self):
        if self.segment[0].xcor() == 600 or self.segment[0].ycor() == 350:
            self.write("GAME OVER.", align="center", font=("Arial", 30, "normal"))
            return False

    def snake_tail(self):
        for i in range(len(self.segment)-1, 0, -1):
            if self.segment[0].pos() == self.segment[i].pos():
                self.write("GAME OVER.", align="center", font=("Arial", 30, "normal"))
                return False
