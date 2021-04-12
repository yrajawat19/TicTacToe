"""***************************************** TIC TAC TOE GAME *******************************************"""
"""*************Global Variables****************"""
Board =['-','-','-','-','-','-','-','-','-']
game_still_going_on = True
winner = None
current_player = "X"
# Function showing Tic Tac Toe board
def Show_Board():
    print(Board[0]," | ",Board[1]," | ",Board[2])
    print(Board[3]," | ",Board[4]," | ",Board[5])
    print(Board[6]," | ",Board[7]," | ",Board[8])
# Function responsible for  handling Turns
def Handle_Turn(player):
    print(player,"'s turn .")
    position = int(input("Enter the position (1-9) : "))
    position = position - 1
    Board[position]= player
    Show_Board()
# Function responsible for running the game
def play_game():
    global winner
    Show_Board()
    while game_still_going_on:
        Handle_Turn(current_player)
        Check_if_game_over()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner," won.")
    elif winner == None :
        print(" Tie .")

# Function responsible for checking if game over or not .
def Check_if_game_over():
    Check_if_win()
    Check_if_tie()
# Function checking if any player won or not
def Check_if_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonal()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return
# Checking Rows in Board for same element X or O
def check_rows():
    global game_still_going_on
    row1 = Board[0] == Board[1] == Board[2]  != "-"
    row2 = Board[3] == Board[4] == Board[5]  != "-"
    row3 = Board[6] == Board[7] == Board[8]  != "-"
    if row1 or row2 or row3:
        game_still_going_on = False
    if row1:
        return Board[0]
    if row2:
        return Board[3]
    if row3:
        return Board[6]
# Checking columns for same elements
def check_columns():
    global game_still_going_on
    column1 = Board[0] == Board[3] == Board[6]  != "-"
    column2 = Board[1] == Board[4] == Board[7]  != "-"
    column3 = Board[2] == Board[5] == Board[8]  != "-"
    if column1 or column2 or column3:
        game_still_going_on = False
    if column1:
        return Board[0]
    if column2:
        return Board[1]
    if column3:
        return Board[2]
# Checking diagonals for same elements
def check_diagonal():
    global game_still_going_on
    diagonal1 = Board[0] == Board[4] == Board[8] != "-"
    diagonal2 = Board[2] == Board[4] == Board[6] != "-"
    if diagonal1 or diagonal2:
        game_still_going_on = False
    if diagonal1:
        return Board[0]
    if diagonal2:
        return Board[2]
# Function responsible for flipping the players
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return True
# Function checking the Tie condition in game .
def Check_if_tie():
    global game_still_going_on
    if "-" not in Board:
        game_still_going_on = False
    return game_still_going_on
# Function call
play_game()


