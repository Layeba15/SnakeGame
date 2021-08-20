import time
from turtle import Screen
from snake import SnakeAppearance
from food import Food
from score import Score

screen = Screen()
screen.title("My Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
snake = SnakeAppearance()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.update()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()
    # Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    for segment in snake.segments:
        if segment == snake.head:
            pass
        else:
            if snake.head.distance(segment) < 10:
                score.reset()
                snake.reset()
screen.exitonclick()
