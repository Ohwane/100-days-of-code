from turtle import Turtle, Screen

tim = Turtle()
tim1 = Turtle()
tim2 = Turtle()
tim3 = Turtle()
tim4 = Turtle()

tim.penup()
tim1.penup()
tim2.penup()
tim3.penup()
tim4.penup()

tim.shape("turtle")
tim1.shape("turtle")
tim2.shape("turtle")
tim3.shape("turtle")
tim4.shape("turtle")

tim1.color("red")
tim2.color("orange")
tim3.color("blue")
tim4.color("yellow")

tim1.setpos(0, 30)
tim2.setpos(0 , 60)
tim3.setpos(0, -30)
tim4.setpos(0, -60)

my_screen = Screen()

def move_forward():
    tim.forward(10)

my_screen.listen()
my_screen.onkey(key = "space", fun = move_forward )
my_screen.exitonclick()