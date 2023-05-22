import pandas
from turtle import Turtle, Screen

image = 'blank_states_img.gif'
screen = Screen()
screen.title('us states game')
screen.addshape(image)
us_map = Turtle(image)

state = Turtle()
state.penup()
state.hideturtle()

data = pandas.read_csv('50_states.csv')
states = data.state
all_states_list = states.to_list()
ques_no = 1
answer = True
guessed_states = []

while answer:
    guess = (screen.textinput(title=f'[{ques_no}/50] Guess the state', prompt="what's another state name")).title()
    if guess == 'Exit':
        states_to_learn = [state for state in all_states_list if state not in guessed_states]
        states_dict = {"states": states_to_learn}
        data = pandas.DataFrame(states_dict)
        data.to_csv("States_to_learn.csv")
        break

    if guess in all_states_list:
        guessed_states.append(guess)
        coordinate = data[data.state == guess]
        state.goto(int(coordinate.x), int(coordinate.y))
        state.write(f'{guess}')
        ques_no += 1

    if ques_no == 51:
        state.goto(0, 0)
        state.write('YOU WIN!', align='center', font=('courier', 40, 'normal'))
        answer = False
        screen.exitonclick()


