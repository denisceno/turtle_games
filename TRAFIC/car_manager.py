from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
y_cordinates = [x for x in range(-250,250,20)]

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        random_chanse = random.randint(1,6)
        if random_chanse == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)


    def movement(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    def level_speed(self):
        self.car_speed += MOVE_INCREMENT












