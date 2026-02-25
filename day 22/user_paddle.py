from turtle import Turtle


class MyPaddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(xcor, ycor)
        self.padY = 40

    def move_up(self):
        self.setpos(self.xcor(), self.ycor() + self.padY)

    def move_down(self):
        self.setpos(self.xcor(), self.ycor() - self.padY)
