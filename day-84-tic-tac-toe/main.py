available_spaces = [
    'TOP LEFT',
    'TOP MIDDLE',
    'TOP RIGHT',
    'MIDDLE LEFT',
    'MIDDLE',
    'MIDDLE RIGHT',
    'BOTTOM LEFT',
    'BOTTOM MIDDLE',
    'BOTTOM RIGHT'
]

ORIGINAL_GAME_BOARD = {
    'TOP LEFT': "",
    'TOP LEFT DIVIDER': '|',
    'TOP MIDDLE': "",
    'TOP RIGHT DIVIDER': '|',
    'TOP RIGHT': "",
    'TOP ROW': '\n---------\n',
    'MIDDLE LEFT': "",
    'MIDDLE LEFT DIVIDER': '|',
    'MIDDLE': "",
    'MIDDLE RIGHT DIVIDER': '|',
    'MIDDLE RIGHT': "",
    'BOTTOM ROW': '\n---------\n',
    'BOTTOM LEFT': "",
    'BOTTOM LEFT DIVIDER': '|',
    'BOTTOM MIDDLE': "",
    'BOTTOM RIGHT DIVIDER': '|',
    'BOTTOM RIGHT': "",
}

def set_game_board(board):

    # Reset Board
    updated_board = ""
    # Rebuild board
    for key in board:
        position = f" {board[key]}"
        updated_board += position

    return updated_board

def check_game(board):
    print('Checking game')

    winner = None

    if board["TOP LEFT"] == current_player and board["TOP MIDDLE"] == current_player and board["TOP RIGHT"] == current_player:
        print('YOU WIN TOP ROW')
        winner = current_player
    elif board["MIDDLE LEFT"] == current_player and board["MIDDLE"] == current_player and board["MIDDLE RIGHT"] == current_player:
        print('YOU WIN MIDDLE ROW')
        winner = current_player
    elif board["BOTTOM LEFT"] == current_player and board["BOTTOM MIDDLE"] == current_player and board["BOTTOM RIGHT"] == current_player:
        print('YOU WIN BOTTOM ROW')
        winner = current_player
    elif board["TOP LEFT"] == current_player and board["MIDDLE LEFT"] == current_player and board["BOTTOM LEFT"] == current_player:
        print('YOU WIN LEFT ROW')
        winner = current_player
    elif board["TOP MIDDLE"] == current_player and board["MIDDLE"] == current_player and board["BOTTOM MIDDLE"] == current_player:
        print('YOU WIN MIDDLE ROW')
        winner = current_player
    elif board["TOP RIGHT"] == current_player and board["MIDDLE RIGHT"] == current_player and board["BOTTOM RIGHT"] == current_player:
        print('YOU WIN RIGHT ROW')
        winner = current_player
    elif board["TOP LEFT"] == current_player and board["MIDDLE"] == current_player and board["BOTTOM RIGHT"] == current_player:
        print('YOU WIN DIAGONAL DOWN')
        winner = current_player
    elif board["TOP RIGHT"] == current_player and board["MIDDLE"] == current_player and board["BOTTOM LEFT"] == current_player:
        print('YOU WIN DIAGONAL UP')
        winner = current_player

    # If there is a winner, stop the game!
    if winner:
        print(f"Congratulations Player {winner}. You won!")
        return True

# PROGRAM START
print('Welcome to Tic Tac Toe')
current_player = "0"
game_is_on = True

current_board = ORIGINAL_GAME_BOARD

while game_is_on:

    # Rebuild gameboard
    printed_board = set_game_board(current_board)
    print(f"Current Board:\n{printed_board}")

    # Have player enter in a new tic tac toe position
    user_input = input(f"Player {current_player}, your turn. Available Options are: {available_spaces}. Enter Position: ").upper().strip()

    # If input is valid, proceed with game
    if user_input in available_spaces:

        current_board[user_input] = f"{current_player}"

        if check_game(current_board):
            game_is_on = False
        elif available_spaces:
            available_spaces.remove(user_input)

        if not available_spaces:
            response = input("Draw! Play again? (Y or N): ").upper()
            if response == "Y":
                printed_board = set_game_board(ORIGINAL_GAME_BOARD)
            else:
                game_is_on = False

        # Switch Player
        if current_player == "0":
            current_player = "X"
        else:
            current_player = "0"

    # Otherwise have user re-enter valid option
    else:
        print('Invalid entry. Try again.')

