import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('dark sea green')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed(10)
        self.new_pos()

    def new_pos(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)
