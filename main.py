from turtle import Screen
import time
from snake import Snake
from food import Food
from screboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("red")
screen.title("Desktop Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorebord = Scoreboard()

screen.listen()
screen.onkey(snake.up, key="w")
screen.onkey(snake.down, key="s")
screen.onkey(snake.left, key="a")
screen.onkey(snake.right, key="d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scorebord.increase_score()
        snake.extend()

    # detecting collisions with walls
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scorebord.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scorebord.reset()
            snake.reset()

screen.exitonclick()
