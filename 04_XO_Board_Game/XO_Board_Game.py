board = [ " ", " ", " ",
          " ", " ", " ",
          " ", " ", " "]

player_1 = input("Choose X or O:").upper()

while player_1 not in ['X', 'O']:
    print("Invalid Choice, Please Choose X or O")
    player_1 = input("Choose X or O:").upper()

if player_1 == 'X':
    player_2 = 'O'
else:
    player_2 = 'X'


print("Player 1 plays as ", player_1)
print("Player 2 plays as ", player_2)
print()

def display_board():
    print("=============")
    print("Enjoy XO Game")
    print("=============")
    print()
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[0]} | {board[1]} | {board[2]} ")

def reset_board():
    for index in range(len(board)):
        board[index] = " "

def get_player_move(player):
    position = int(input("Choose a position form 1 to 9: "))

    while board[position -1] != " ":
        print("Choose a empty position from 1 to 9:")
        position = int(input("Choose an empty position from 1 to 9:"))

    board[position -1] = player
    display_board()

def check_winner(player):
    winning_combination = [
                            [0,1,2], [3,4,5], [6,7,8],
                            [0,3,6], [1,4,7], [2,5,8],
                            [0,4,8], [2,4,6]
                          ]

    for option in winning_combination:
        if all(board[index] == player for index in option):
            return True
    return False

def play_game(player_1, player_2):
    display_board()
    while True:
        get_player_move(player_1)

        if check_winner(player_1):
            print("Game is Over and Player 1 is the Winner!")
            break

        if " " not in board:
            print("Game is a Draw!")
            print("Start New Game!")
            reset_board()
            display_board()
            continue

        get_player_move(player_2)

        if check_winner(player_2):
            print("Game is Over and Player 2 is the Winner!")
            break

        if " " not in board:
            print("Game is a Draw!")
            print("Start New Game!")
            reset_board()
            display_board()
            continue


play_game(player_1,player_2)