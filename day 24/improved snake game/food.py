from turtle import Turtle
import random
import time


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.food_store = []

    def create_food(self):
        self.hideturtle()
        self.speed("fastest")
        self.shape("square")
        self.color("purple")
        self.shapesize(0.5)
        self.penup()
        self.goto(random.randint(-400,400),
                      random.randint(-250,250))
        self.showturtle()
        self.food_store.append(self)





