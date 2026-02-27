from snake import Snake
from turtle import Screen
from scoreboard import Scoreboard
from food import Food
import time

snake = Snake()
food = Food()
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

food.create_food()

snake.create_snake()

score = Scoreboard()


while myloop:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segment[0].distance(food.food_store[0]) < 20:
        # self.food_store[0].hideturtle()
        # self.food_store.pop()
        food.create_food()
        snake.add_segment()
        score.score_increase()

    if snake.segment[0].xcor() == 600:
        score.reset()
        snake.reset()
    elif snake.segment[0].ycor() == 360:
        score.reset()
        snake.reset()
    elif snake.segment[0].xcor() == -600:
        score.reset()
        snake.reset()
    elif snake.segment[0].ycor() == -360:
        score.reset()
        snake.reset()
    else:
        pass

    for i in range(1, len(snake.segment)):
        if snake.segment[0].distance(snake.segment[i]) < 5:
            score.reset()
            snake.reset()
