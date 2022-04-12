# game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

# if game is still going
game_still_going = True

# who won?or tie?
winner = None

# whos turn is it
current_player = "X"


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# play a game of tic tac toe
def play_game():
    # display the initial board
    display_board()

    while game_still_going:
        # handle a single turn
        handle_turn(current_player)

        # check if game has ended
        check_if_game_over()

        # flip to the other player
        flip_player()

    # the game has ended
    if winner == "X" or winner == "O":
        print(winner + "won.")

    elif winner == None:
        print("tie.")


def handle_turn(current_player):
    print(current_player + "'s turn")
    position = input("choose a position from 0 to 8: ")


    valid = False
    while not valid:

        while position not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
          position = input("invalid input.please choose a position from 0 to 8: ")

        position = int(position)

        if board[position] == "-":
            valid = True
        else:
            print("you cant go there.Go again")

    board[position] = current_player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # set uo global variable
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner


    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None

    return


def check_rows():
    global game_still_going

    # check if any row has same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any row has a match,flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner X or O
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return


def check_columns():
    # check if any column has same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any column has a match,flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner X or O
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return


def check_diagonals():
    # check if any diagonal has same value
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    # if any diagonal has a match,flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner X or O
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]

    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False

    return


def flip_player():
    # global variables we need
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()

