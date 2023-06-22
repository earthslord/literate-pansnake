from turtle import Screen
import time
from snake import Snake
from food import Food
from scores import Scoreboard
screen = Screen()
screen.screensize(800, 800)
screen.bgcolor("black")
screen.title("SNAKE GAME")
is_on = True
screen.tracer(0)

snake = Snake()
food = Food()
sb = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_on:
    # Making snake move as one
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.new_pos()
        sb.score_plus()
        snake.grow()
    # Wall collision
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        sb.reset_sb()
        snake.come_home_perry()
    # Tail collision
    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 15:
            sb.reset_sb()
            snake.come_home_perry()


screen.exitonclick()
