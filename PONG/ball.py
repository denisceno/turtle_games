from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.moove_speed = 0.1


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def ball_bounc(self):
        self.y_move *= -1


    def paddle_bounc(self):
        self.x_move *= -1
        self.moove_speed *= 0.8

    def reset_position(self):
        self.goto(0,0)
        self.x_move *= -1


