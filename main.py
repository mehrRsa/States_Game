import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
imag = "blank_states_img.gif"
turtle.addshape(imag)
turtle.shape(imag)


guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States corrext", prompt="What's another state name?").title()

    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()


    if answer_state == "Exit":
        missing_list = []
        for state in all_states:
            if state not in guessed_states:
                missing_list.append((state))
        print(missing_list)

        spread_sheet = pandas.DataFrame(missing_list)
        spread_sheet.to_csv("missing_states")

        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

