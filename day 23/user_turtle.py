from turtle import Turtle


class CrossTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setheading(90)
        self.penup()
        self.y_move = -330
        self.setpos(0, self.y_move)
        self.showturtle()
        self.shape("turtle")
        self.color("black")

    def tur_up(self):
        self.forward(20)

    def tur_down(self):
        self.backward(20)

    def reset_turtle(self):
        self.goto(0, self.y_move)

