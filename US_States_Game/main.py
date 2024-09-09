import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
data['state'] = data['state'].str.lower()

s_count = 0
while True:
    answer = screen.textinput(title=f"Guess the state {s_count}/50", prompt="Try finding a state").lower()
    t1 = turtle.Turtle()
    t1.hideturtle()
    t1.penup()
    if answer in data["state"].values:
        row = data[data["state"] == answer]
        x = row["x"].values[0]
        y = row["y"].values[0]
        t1.goto(x, y)
        t1.write(answer.title(), align="center", font=("Arial", 16, "normal"))
        s_count += 1
