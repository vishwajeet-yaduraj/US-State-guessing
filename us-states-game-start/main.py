from Names import Names
import pandas as pd
import turtle

data = pd.read_csv('50_states.csv')
state_list = data['state'].to_list()

screen = turtle.Screen()
screen.title("US States Game")
image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)

input_states = []

is_game_on = True

while is_game_on:
    if len(input_states) == len(state_list):
        is_game_on = False
    text_input = screen.textinput(prompt="Name any of the states",
                                  title=f"{len(input_states)}/{len(state_list)}: Guess the sates").title()
    if text_input == 'Exit':
        is_game_on = False

    if text_input in state_list and text_input not in input_states:
        input_states.append(text_input)
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state = data[data.state == text_input]
        timmy.goto(int(state.x), int(state.y))
        timmy.write(text_input)

# States to learn .csv


for states in state_list:
    if states in input_states:
        state_list.remove(states)

data = pd.DataFrame(state_list)

data.to_csv("Missing_states.csv")
