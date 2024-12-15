import turtle
import pandas
from label import StateLabel

screen = turtle.Screen()
screen.title("U.S. States Game")

IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# def get_mouse_click_coor(x,y):
#     print(x, y)
#
# # Listener
# turtle.onscreenclick(get_mouse_click_coor)
# # Alternative way of keeping screen open even if code has finished. Alternative to "exitonclick"
# turtle.mainloop()
# screen.exitonclick()

# TODO: Read coordinates from file
# Ask user for input

game_on = True
found_states = []
prompt = "Guess a State name!"

while game_on:

    user_input = screen.textinput(title=f"Guess the State {len(found_states)}/50", prompt=prompt).title()

    # Convert CSV into data frame so we can use pandas library
    us_state_data_frame = pandas.read_csv("50_states.csv")

    # Find the row where the state is equal to user's input
    selected_state = us_state_data_frame[us_state_data_frame["state"] == user_input]
    print(selected_state)

    # Check if it is a valid state
    if selected_state.empty:
        prompt = "Not a valid guess! Guess Again."
        print('WRONG')
    elif user_input in found_states:
        print('Already Guessed')
        prompt = "Already Guessed! Guess Again."
    else:
        print('RIGHT')
        prompt = "Good Job! Guess Again."
        # Write new turtle on screen with state coordinates
        new_label = StateLabel(selected_state)
        found_states.append(selected_state.state.item())

        if len(found_states) == 50:
            game_on = False

# TODO keep track of number of states that have been guesses
# Once user has entered value, determine if they have the state right and then determine which coordinate to show up on map

