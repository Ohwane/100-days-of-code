from turtle import Turtle, Screen
from ball import Ball
from user_paddle import MyPaddle
from center_dash import CenterDash
import time
from scoreboard import ScoreBoard


my_screen = Screen()
my_screen.setup(850, 700)
my_screen.bgcolor("black")
my_screen.title("pong")

user_paddle1 = MyPaddle(-400, 0)
user_paddle2 = MyPaddle(400, 0)


def starting_delay():
    tim = Turtle()
    tim.hideturtle()
    for timer in range(3, -1, -1):
        tim.color("red")
        tim.write(f"{timer}", align="center", font=("Arial", 90, "bold"))
        time.sleep(1)
        tim.clear()


score = ScoreBoard()
CenterDash()
ball = Ball()
time.sleep(1)
starting_delay()

my_screen.listen()
my_screen.onkey(key="w", fun=user_paddle1.move_up)
my_screen.onkey(key="s", fun=user_paddle1.move_down)
my_screen.onkey(key="Up", fun=user_paddle2.move_up)
my_screen.onkey(key="Down", fun=user_paddle2.move_down)

game_on = True


while game_on:
    time.sleep(0.01)
    ball.move()

    if ball.distance(ball.xcor(), 350) < 20 or ball.distance(ball.xcor(), -350) < 20:
        ball.wall_bounce()

    elif ball.distance(user_paddle1) < 60 and ball.xcor() < -380:
        ball.x_move += 1
        ball.y_move += 1
        ball.paddle_bounce()

    elif ball.distance(user_paddle2) < 60 and ball.xcor() > 380:
        ball.x_move += 1
        ball.y_move += 1
        ball.paddle_bounce()

    elif ball.xcor() > 450:
        score.add_left()
        ball.hideturtle()
        ball.restart()
        ball.showturtle()
        time.sleep(1)
        ball.paddle_bounce()

    elif ball.xcor() < -450:
        score.add_right()
        ball.hideturtle()
        ball.restart()
        ball.showturtle()
        time.sleep(1)
        ball.paddle_bounce()

    else:
        pass


my_screen.exitonclick()
