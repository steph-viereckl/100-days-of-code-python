import turtle
import pandas
from label import StateLabel

screen = turtle.Screen()
screen.title("U.S. States Game")

IMAGE = "blank_states_img.gif"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# # Alternative way of keeping screen open even if code has finished. Alternative to "exitonclick"
# turtle.mainloop()
# screen.exitonclick()

game_on = True
found_states = []
prompt = "Guess a State name!"

# Convert CSV into data frame so we can use pandas library
us_state_data_frame = pandas.read_csv("50_states.csv")

while len(found_states) < 50:

    user_input = screen.textinput(title=f"Guess the State {len(found_states)}/50", prompt=prompt).title()

    # Find the row where the state is equal to user's input
    selected_state = us_state_data_frame[us_state_data_frame["state"] == user_input]

    # Break out of while loop and close game
    if user_input == "Exit":

        # Create "states_to_learn.csv" that includes all states the user has not guessed

        states_to_learn = [state for state in us_state_data_frame.state if state not in found_states]
        # for state in us_state_data_frame.state:
        #     if state not in found_states:
        #         states_to_learn.append(state)

        states_to_learn_df = pandas.DataFrame(states_to_learn, columns=["state"])
        states_to_learn_df.to_csv("states_to_learn.csv")
        break

    # Check if it is a valid entry (data frame will be empty if there is no matching state)
    elif selected_state.empty:
        prompt = "Not a valid guess! Guess Again."

    # Check if state has already been guessed
    elif user_input in found_states:
        prompt = "Already Guessed! Guess Again."

    # Otherwise, it is a correct guess
    else:
        prompt = "Good Job! Guess Again."
        # Write new turtle on screen with state coordinates
        new_label = StateLabel(selected_state)
        # Add guessed state into the list of already guessed states
        found_states.append(selected_state.state.item())
