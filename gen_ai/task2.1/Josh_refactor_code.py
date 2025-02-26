# Tic Tac Toe game

import random

def show_board():
    print(" ----------- ")
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
        print(" ----------- ")

def count_board(symbol):
    return board.count(symbol)

def check_winner():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return 'D' if count_board('X') + count_board('O') == 9 else 'C'

def get_x_player_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-9): ")) - 1
            if choice < 0 or choice > 8 or board[choice] in ('X', 'O'):
                print("Invalid choice, try again.")
            else:
                board[choice] = 'X'
                break
        except ValueError:
            print("Please enter a valid number.")

def get_o_player_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-9): ")) - 1
            if choice < 0 or choice > 8 or board[choice] in ('X', 'O'):
                print("Invalid choice, try again.")
            else:
                board[choice] = 'O'
                break
        except ValueError:
            print("Please enter a valid number.")

def get_computer_choice():
    while True:
        choice = random.randint(0, 8)
        if board[choice] not in ('X', 'O'):
            board[choice] = 'O'
            break

def computer_vs_player():
    global board
    board = [str(i+1) for i in range(9)]
    while True:
        show_board()
        if count_board('X') == count_board('O'):
            print("Player X, make a selection:")
            get_x_player_choice()
        else:
            get_computer_choice()
        winner = check_winner()
        if winner in ('X', 'O'):
            show_board()
            print(f"{winner} won!! GameOver")
            break
        elif winner == 'D':
            print("It is a tie!!")
            break

def player_vs_player():
    global board
    board = [str(i+1) for i in range(9)]
    while True:
        show_board()
        if count_board('X') == count_board('O'):
            print("Player X, make a selection:")
            get_x_player_choice()
        else:
            print("Player O, make a selection:")
            get_o_player_choice()
        winner = check_winner()
        if winner in ('X', 'O'):
            show_board()
            print(f"{winner} won!! GameOver")
            break
        elif winner == 'D':
            print("It is a tie!!")
            break

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Single Player.")
        print("2. Multiplayer.")
        print("3. Exit Game.")
        mode = input("Select an option: ")
        if mode == '1':
            computer_vs_player()
        elif mode == '2':
            player_vs_player()
        else:
            print("Please select a valid game mode!")

if __name__ == "__main__":
    print("##################################")
    print("#   Welcome to TicTacToe Game!   #")
    print("##################################\n")
    main_menu()
