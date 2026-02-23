from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.default_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.score_update()

    def score_update(self):
        self.write(f"Score: {self.default_score}", False, "left", ("Arial", 20, "bold"))

    def score_increase(self):
        self.clear()
        self.default_score += 1
        self.score_update()
