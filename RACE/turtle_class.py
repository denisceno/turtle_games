from turtle import Turtle, Screen
import random
class Turtle1(Turtle):
    def __init__(self,t_color, x, y):
        super().__init__()
        self.t_color = t_color
        self.x = x
        self.y = y
        self.penup()
        self.color(t_color)
        self.goto(x,y)
        self.shape("turtle")

    def t_speed(self):
        rnd = random.randint(1,20)
        self.forward(rnd)


