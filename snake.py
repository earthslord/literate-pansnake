from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment((-20*i, 0))

    def add_segment(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.snake.append(t)

    def grow(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            nx = self.snake[i - 1].xcor()
            ny = self.snake[i - 1].ycor()
            self.snake[i].goto(nx, ny)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != -90:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(-90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def come_home_perry(self):
        for s in self.snake:
            s.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
