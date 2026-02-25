from turtle import Turtle, Screen
from user_turtle import CrossTurtle
from cars import Cars
from level_board import Score
import time

screen = Screen()
screen.setup(700, 700)
screen.tracer(0)
screen.listen()

score = Score()
cross_turtle = CrossTurtle()

cars = Cars()

screen.onkey(cross_turtle.tur_up, "Up")
screen.onkey(cross_turtle.tur_down, "Down")
game_on = True

while game_on:

    time.sleep(0.1)
    screen.update()

    cars.create_car()
    if cross_turtle.ycor() > 250:
        cars.increase_speed()
        cross_turtle.reset_turtle()
        score.score_update()

    for i in cars.all_cars:
        if cross_turtle.distance(i) < 20:
            game_on = False
            Turtle().write("GAME OVER.", align="center", font=("Arial", 60, "bold"))

        if i.xcor() < -300:
            i.hideturtle()
            cars.all_cars.remove(i)
    cars.drive()
    # for car_round in range(6):




screen.exitonclick()
