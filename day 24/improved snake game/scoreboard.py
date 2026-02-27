from turtle import Turtle
from snake import Snake


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as file:
            data = int(file.read())
        self.default_score = 0
        self.high_score = data
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.write(f"Score: {self.default_score} |  Highscore: {self.high_score}", False, "left", ("Arial", 20, "bold"))

    def score_increase(self):
        self.clear()
        self.default_score += 1
        self.score_update()

    def reset(self):
        if self.default_score > self.high_score:
            self.high_score = self.default_score
        self.default_score = 0
        self.clear()
        self.score_update()
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")
