# from turtle import Turtle, Screen
# import random

# timmy=Turtle()
# timmy.shape("turtle")

# my_screen= Screen()


# # Count= 50
# # yeah=True
# # while yeah:

# for i in range(50):
#     move= [40,70,100,130]
#     directions=[timmy.left(90), timmy.right(180),timmy.left(180)]
#     color=["green", "red", "maroon", "blue", "purple","black"]
#     timmy.color(random.choice(color))
#     random.choice(directions)
#     timmy.forward(random.choice(move))
#     # count-=1
#     # if Count==0:
#     #     yeah=False

# my_screen.exitonclick()

from turtle import Turtle, Screen
import random

timmy= Turtle()
timmy.shape("turtle")
timmy.speed(10)
my_screen=Screen()

directions= [90,180,270,360]
timmy.pensize(10)
colours= ["orange", "blue", "black", "yellow", "purple", "red", "green", "grey"]
for i in range(200):
    timmy.setheading(random.choice(directions))
    timmy.color(random.choice(colours))
    timmy.forward(30)
my_screen.exitonclick()