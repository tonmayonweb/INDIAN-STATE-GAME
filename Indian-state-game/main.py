import turtle
import pandas
screen = turtle.Screen()
timmy = turtle.Turtle()
screen.title("U.S. States Game")
image = "./data/indiamap.gif"
screen.setup(width=700, height=700)
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)


state_data = pandas.read_csv("./data/india-states.csv")
state_name = state_data.state
state_list = state_name.to_list()  # state lists

gameon = True
count = 0
guessed_state = []
while gameon:
    answer_state = turtle.textinput(title=f"{count}/33 Guess the states", prompt="Whats another states name")
    answer_state_title = answer_state.title()
    guessed_state.append(answer_state_title)
    if answer_state_title == "Exit":
        missing_state = [state for state in state_list if state not in guessed_state]   # adding not guessed states
        # to the list to create a csv file
        data = pandas.DataFrame(missing_state)
        data.to_csv("data/states_to_learn.csv")
        break
    if answer_state_title in state_list:
        count += 1
        state_row = state_data[state_data.state == answer_state_title]
        state_row_dict = state_row.to_dict()
        x_position = (state_row_dict["x"][state_list.index(answer_state_title)])
        y_position = (state_row_dict["y"][state_list.index(answer_state_title)])
        timmy.penup()
        timmy.hideturtle()
        timmy.goto(x=x_position, y=y_position)
        timmy.write(f"{answer_state_title}", False, "center", font=('Ariel', 8, 'bold'))
    if count == 33:
        timmy.goto(0, 0)
        timmy.write(f"Congratulation, you guessed all of the 33 states", False, "center", font=('Ariel', 24, 'bold'))
        break
# turtle.mainloop()
