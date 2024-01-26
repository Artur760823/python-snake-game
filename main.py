from turtle import Screen
import time
from snake import Snake
from food import Food
from screboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Desktop Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorebord = Scoreboard()

screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.right, key="Right")

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
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        game_is_on = False
        scorebord.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scorebord.game_over()

screen.exitonclick()
