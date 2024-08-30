import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car = CarManager()
score_board = Scoreboard()


screen.listen()
screen.onkey(player.movement, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.new_car()
    car.movement()

    for cars in car.all_cars:
        if cars.distance(player) < 20 :
            game_is_on = False
            score_board.game_over()

    if player.nex_level():
        player.go_to_start()
        car.level_speed()
        score_board.new_level()




screen.exitonclick()