from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.org_score = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.speed("fastest")
        self.goto(-300, 300)
        self.write(f"LEVEL: {self.org_score}", font=("Arial", 15, "bold"))

    def score_update(self):
        self.clear()
        self.org_score += 1
        self.write(f"LEVEL: {self.org_score}", font=("Arial", 30, "bold"))
