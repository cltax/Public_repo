#Setup of the board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#Function to print the board
def print_board():
    print(board[0]+" | "+board[1]+" | "+board[2])
    print(board[3]+" | "+board[4]+" | "+board[5])
    print(board[6]+" | "+board[7]+" | "+board[8])

#Function to handle turns
def take_turn(player):
    listA = [str(num) for num in range(1,10)]
    #listA = ["1","2","3","4","5","6","7","9"]
    print(player + "'s turn.")
    position = input("Choose a position form 1-9: ")
    while position not in listA:
        position = input("Invalid input! Choose a position between 1-9: ")
    position = int(position) - 1
    while board[position] != "-":
        position = int(input("Position already taken. Please choose a different one: ")) - 1
    board[position] = player
    print_board()

#Function to check if the game is over
def check_game_over():
    #Check for a win
    if ((board[0] == board[1] == board[2] != "-") or 
        (board[3] == board[4] == board[5] != "-") or
        (board[6] == board[7] == board[8] != "-") or
        (board[0] == board[4] == board[8] != "-") or
        (board[2] == board[4] == board[6] != "-") or
        (board[0] == board[3] == board[6] != "-") or
        (board[1] == board[4] == board[7] != "-") or
        (board[2] == board[5] == board[8] != "-")
    ):
        return "win"
    #Check for a tie
    elif "-" not in board:
        return "tie"
    else:
        return "play"

#Main Game
def play_game():
    print_board()
    current_player = "X"
    game_over = False
    while not game_over:
        take_turn(current_player)
        game_result = check_game_over()
        if game_result == "win":
            print(current_player + " wins!")
        elif game_result == "tie":
            print("It's a tie!")
        else:
            #Switch to the other player
            current_player = "O" if current_player == "X" else "X"

#Start game
play_game()

