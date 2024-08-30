from turtle import Turtle, Screen
import random
from turtle_class import Turtle1


screen = Screen()
screen.setup(500,500)
bet = screen.textinput("bet","chose a color")
colors = ["blue","red","green","yellow","black", "purple"]
turtles = []
y = 200
for te in range(0,6):
    te = Turtle1(colors[te],-230,y)
    y -= 50
    turtles.append(te)
is_game = True
while is_game:
    for t in turtles:
        if t.xcor() > 230:
            is_game = False
            if t.color == bet:
                print("you win")
            else:
                print(f"you losse . The {t.t_color} win")
                break
        t.t_speed()








screen.exitonclick()

