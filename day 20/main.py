from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard
import time

snake = Snake()
my_screen = Screen()
my_screen.setup(1200, 720)
my_screen.bgcolor("black")
my_screen.tracer(0)

my_screen.listen()
my_screen.onkey(key="f", fun=my_screen.exitonclick)
my_screen.onkey(key="w", fun=snake.go_up)
my_screen.onkey(key="a", fun=snake.go_left)
my_screen.onkey(key="s", fun=snake.go_down)
my_screen.onkey(key="d", fun=snake.go_right)

myloop = True

snake.create_food()

snake.create_snake()

score = Scoreboard()


while myloop:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segment[0].distance(snake.food_store[0]) < 20:
        # self.food_store[0].hideturtle()
        # self.food_store.pop()
        snake.create_food()
        snake.add_segment()
        score.score_increase()

    if snake.segment[0].xcor() == 600:
        snake.color("white")
        snake.setpos(0, 0)
        snake.write("GAME OVER.", align="center", font=("Arial", 60, "normal"))
        my_screen.exitonclick()
    elif snake.segment[0].ycor() == 360:
        snake.color("white")
        snake.setpos(0, 0)
        snake.write("GAME OVER.", align="center", font=("Arial", 60, "normal"))
        my_screen.exitonclick()
    elif snake.segment[0].xcor() == -600:
        snake.color("white")
        snake.setpos(0, 0)
        snake.write("GAME OVER.", align="center", font=("Arial", 60, "normal"))
        my_screen.exitonclick()
    elif snake.segment[0].ycor() == -360:
        snake.color("white")
        snake.setpos(0, 0)
        snake.write("GAME OVER.", align="center", font=("Arial", 60, "normal"))
        my_screen.exitonclick()
    else:
        pass

    for i in range(1, len(snake.segment), 1):
        if snake.segment[0].distance(snake.segment[i]) < 10:
            snake.color("white")
            snake.setpos(0, 0)
            snake.write("GAME OVER.", align="center", font=("Arial", 30, "normal"))
            my_screen.exitonclick()
