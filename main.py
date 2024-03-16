import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

csv_data = pandas.read_csv("50_states.csv")

states_list = csv_data["state"].to_list()
xcor_list = csv_data["x"].to_list()
ycor_list = csv_data["y"].to_list()

correct_guesses = []

while len(correct_guesses) < 50:

    state_answer = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="Name A State").title()

    if state_answer == "Exit":
        break

    if states_list.__contains__(state_answer):
        index = states_list.index(state_answer)
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(xcor_list[index], ycor_list[index])
        text.write(state_answer, align="center", font=("Arial", 10, "normal"))
        if not correct_guesses.__contains__(state_answer):
            correct_guesses.append(state_answer)

states_to_study = []
for state in states_list:
    if state not in correct_guesses:
        states_to_study.append(state)
states_dataframe = pandas.DataFrame(states_to_study)
states_dataframe.to_csv("states_to_review.csv")

turtle.mainloop()
