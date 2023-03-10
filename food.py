from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.atualiza()


    def atualiza(self):
        x_aleatorio = randint(-280,280)
        y_aleatorio = randint(-280,280)
        self.goto(x_aleatorio, y_aleatorio)
