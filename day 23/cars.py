from turtle import Turtle
import random
import time


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.CAR_SPEED = 20
        self.all_cars = []

        self.colors = ["red", "blue", "orange", "yellow", "green", "purple"]

    def create_car(self):
        tom_cars = Turtle()
        tom_cars.speed("fastest")
        tom_cars.hideturtle()
        tom_cars.penup()
        tom_cars.color(random.choice(self.colors))
        tom_cars.setheading(180)
        tom_cars.shapesize(20)
        tom_cars.shapesize(1, 2)
        tom_cars.shape("square")
        x_cor = random.randint(700, 850)
        y_cor = random.randint(-250, 250)
        tom_cars.setpos(x_cor, y_cor)
        tom_cars.showturtle()
        self.all_cars.append(tom_cars)
        print(self.all_cars)

    def drive(self):
        for i in self.all_cars:
            i.forward(self.CAR_SPEED)
            # self.remove_car()

    def increase_speed(self):
        self.CAR_SPEED += 10
    # def remove_car(self):
    #     for i in range(0, len(self.all_cars)-1):
    #         if self.all_cars[i].xcor() < -350:
    #             self.all_cars[i].clear()
    #             # self.all_cars.remove(self.all_cars[i])
