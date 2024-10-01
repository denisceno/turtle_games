from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 600)
user_bet = screen.textinput("Make your ber", "Which turtle will win the race")
print(f"You bet on the {user_bet} turtle")
colors = ["red", "blue", "yellow", "green", "purple", "orange", "black", "cyan", "silver", "gold"]
positin = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]
turtles = []


def turles(t_color, x, y):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(t_color)
    turtle.goto(x, y)
    return turtle


for i in range(0, 10):
    turtle_n = turles(t_color=colors[i], x=-230, y=positin[i])
    turtles.append(turtle_n)

race_on = True

while race_on:
    for t in turtles:
        if t.xcor() > 211:
            race_on = False
            winner = t.pencolor()
            if winner == user_bet:
                print(f"You WON. The {winner} turtle won the race")
            else:
                print(f"You LOSE. The {winner} turtle won the race")
        distance = random.randint(1, 10)
        t.forward(distance)

screen.exitonclick()
