# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append((int(row[1])))
#     print(temperature)


import pandas

# data = pandas.read_csv("weather_data.csv")
# # temp_dict = data["temp"].to_dict()
# # print(temp_dict)
#
# # print(len(data["temp"]))
# #
# # temp_list = data["temp"].to_list()
# # mean = sum(temp_list) / len(temp_list)
# # print(mean)
# #
# # mean2 = data["temp"].mean()
# # print(mean2)
# #
# # max = data["temp"].max()
# # print(max)
#
#
# highest_temp = (data[data.temp == data.temp.max()])
# print(highest_temp)

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# gray = []
# black = []
# cinnamon = []
#
# primary_fur_color = data["Primary Fur Color"].tolist()
# # print(primary_fur_color)
#
# black_fur_count = len(data[data["Primary Fur Color"] == "Black"])
# gray_fur_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_fur_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
#
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "count": [black_fur_count, gray_fur_count, cinnamon_fur_count]
# }
#
# print(data_dict)
#
# new_data_frame = pandas.DataFrame(data_dict)
# new_data_frame.to_csv("fur_colors_data")

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

