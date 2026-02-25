from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.score_update()

    def score_update(self):
        self.write(f"{self.left_score}    {self.right_score}", align="center", font=("Arial", 40, "bold"))

    def add_left(self):
        self.clear()
        self.left_score += 1
        self.score_update()

    def add_right(self):
        self.clear()
        self.right_score += 1
        self.score_update()
