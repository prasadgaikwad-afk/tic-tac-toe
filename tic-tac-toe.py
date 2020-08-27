board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_", ]


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


game_still_going = True

winner = None

current_player = "x"


def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "x" or winner == "o":
        print(winner + "WON.")
    elif winner == None:
        print("TIE.")


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner

    row_winner = check_row()

    cloumn_winner = check_column()

    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner
    elif cloumn_winner:
        winner = cloumn_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return


def check_row():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

    return


def check_column():
    global game_still_going
    cloumn_1 = board[0] == board[3] == board[6] != "_"
    cloumn_2 = board[1] == board[4] == board[7] != "_"
    cloumn_3 = board[2] == board[5] == board[8] != "_"
    if cloumn_1 or cloumn_2 or cloumn_3:
        game_still_going = False
    if cloumn_1:
        return board[0]
    elif cloumn_2:
        return board[1]
    elif cloumn_3:
        return board[2]

    return


def check_diagonal():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[2] == board[4] == board[6] != "_"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:

        return board[6]

    return


def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going = False

    return


def flip_player():
    global current_player
    if current_player == "x":
        current_player = "o"

    elif current_player == "o":
        current_player = "x"

    return


def handle_turn(player):
    print(player + "'s  Turn.")
    position = input("Choose a position to 1 to 9: ")
    valid = False

    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input.  Choose a position to 1 to 9: ")

        position = int(position) - 1
        if board[position] == "_":
            valid = True
        else:
            print("You cnt go there.  Try again")

    board[position] = player
    display_board()


play_game()