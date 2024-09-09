import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
all_states = data['state'].to_list()

correct_a = []
while len(correct_a) < 50:
    answer = screen.textinput(title=f"Guess the state {len(correct_a)}/50", prompt="Try finding a state").title()
    if answer == "Exit":
        not_found_states = []
        for x in all_states:
            if x not in correct_a:
                not_found_states.append(x)
        new_csv = pd.DataFrame(not_found_states)
        new_csv.to_csv("States_to_learn.csv")
        break

    t1 = turtle.Turtle()
    t1.hideturtle()
    t1.penup()
    if answer in data["state"].values:
        correct_a.append(answer)
        row = data[data["state"] == answer]
        x = row["x"].values[0]
        y = row["y"].values[0]
        t1.goto(x, y)
        t1.write(answer.title())
