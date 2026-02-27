from turtle import Turtle
# from food import Food


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segment = []
        self.MOVE_DISTANCE = 20
        # self.go_up()
        # self.go_down()
        # self.go_left()
        # self.go_right()

    def create_snake(self):
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for i in positions:
            tim = Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(i)
            self.segment.append(tim)

    def add_segment(self):
        # self.seg_len += 1
        tim = Turtle("square")
        tim.speed("fastest")
        tim.hideturtle()
        tim.color("white")
        tim.penup()
        self.segment.append(tim)
        tim.showturtle()
    # def rem_snakefood(self):

    def move(self):
        for i in range(len(self.segment)-1, 0, -1):
            new_xcor = self.segment[i-1].xcor()
            new_ycor = self.segment[i-1].ycor()
            self.segment[i].goto(new_xcor, new_ycor)
        self.segment[0].forward(self.MOVE_DISTANCE)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()

    def go_up(self):
        if self.segment[0].heading() == 270:
            pass
        else:
            self.segment[0].setheading(90)

    def go_down(self):
        if self.segment[0].heading() == 90:
            pass
        else:
            self.segment[0].setheading(270)

    def go_left(self):
        if self.segment[0].heading() == 0:
            pass
        else:
            self.segment[0].setheading(180)

    def go_right(self):
        if self.segment[0].heading() == 180:
            pass
        else:
            self.segment[0].setheading(0)

