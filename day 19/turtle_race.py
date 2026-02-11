from turtle import Turtle, Screen
import random

race_turtles = []


def start_game():
    turtle_num = my_screen.numinput(title="Turtle Race Bet", prompt="Welcome to the Turtle Race! "
                                                                         "How many Turtles do you want in this race?"
                                                                         " select 6 At most")
    act = True
    while act:
        if turtle_num > 6:
                act1 = True
                while act1:
                    an_turtlenum = my_screen.numinput(title="Too high", prompt="Too high. Input a value less than 7")
                    turtle_num = an_turtlenum
                    if turtle_num <= 6:
                        act1 = False
                act = False
        elif turtle_num <= 6:
            act = False

        # else:
        #     a_turtletext = int(my_screen.textinput(title="Non number", prompt="Not a number. Enter a number."))
        #     turtle_num = a_turtletext
    myx = -450
    myy = -350
    colours = ["red", "orange", "blue", "yellow", "purple", "green"]
    for i in range(int(turtle_num)):
        tim = Turtle()
        tim.penup()
        tim_color = random.choice(colours)
        race_turtles.append(tim_color)
        tim.color(tim_color)
        colours.remove(tim_color)
        tim.shape("turtle")
        tim.setposition(x=myx, y=myy)
        myy+=130
        # race_turtles.append(f"{i}")
        # race_turtles[i] = Turtle().color(random.choice(colours))
        # race_turtles[i](Turtle.setposition(myx, myy))

    bet = my_screen.textinput(title="Place Bet", prompt="Now place your bet for what turtle will win. Enter the "
                                                            "color")

    print(tim)


    # tim = Turtle(shape="turtle")
    # tim1 = Turtle()
    # tim2 = Turtle()
    # tim3 = Turtle()
    # tim4 = Turtle()
    pass

ti= Turtle()

ti1 = Turtle()

ti2 = Turtle()
turt = (Turtle(), Turtle(), Turtle())
# tim.penup()
# tim1.penup()
# tim2.penup()
# tim3.penup()
# tim4.penup()
#
# tim.shape("turtle")
# tim1.shape("turtle")
# tim2.shape("turtle")
# tim3.shape("turtle")
# tim4.shape("turtle")
#
# tim1.color("red")
# tim2.color("orange")
# tim3.color("blue")
# tim4.color("yellow")
#
# tim1.setpos(0, 30)
# tim2.setpos(0 , 60)
# tim3.setpos(0, -30)
# tim4.setpos(0, -60)

# def move_forward():
#     tim.forward(10)
my_screen = Screen()
my_screen.setup(height=800, width=1000)



start_game()
print(race_turtles)
my_screen.listen()
# my_screen.onkey(key = "space", fun = move_forward )
my_screen.exitonclick()
