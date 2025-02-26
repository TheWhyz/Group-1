# Tic Tac Toe game

import random

def show_board():
    print("\n ----------- ")
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
        print(" ----------- ")

def count_board(symbol):
    return board.count(symbol)

def check_winner():
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), 
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  
        (0, 4, 8), (2, 4, 6)            
    ]
    
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] in ('X', 'O'):
            return board[a]

    return 'D' if all(cell in ('X', 'O') for cell in board) else 'C'

def get_player_choice(symbol):
    while True:
        try:
            choice = int(input(f"Player {symbol}, enter your choice (1-9): ")) - 1
            if 0 <= choice <= 8 and board[choice] not in ('X', 'O'):
                board[choice] = symbol
                break
            else:
                print("Invalid choice, try again.")
        except ValueError:
            print("Please enter a valid number.")

def get_computer_choice():
    best_moves = [4, 0, 2, 6, 8, 1, 3, 5, 7]  # Prioritize center, corners, then edges

    # Check if computer can win in the next move
    for i in range(9):
        if board[i] not in ('X', 'O'):
            board[i] = 'O'
            if check_winner() == 'O':
                return
            board[i] = str(i + 1)  # Undo move

    # Check if player can win and block them
    for i in range(9):
        if board[i] not in ('X', 'O'):
            board[i] = 'X'
            if check_winner() == 'X':
                board[i] = 'O'
                return
            board[i] = str(i + 1)  # Undo move

    # Pick the best available move
    for move in best_moves:
        if board[move] not in ('X', 'O'):
            board[move] = 'O'
            return

def computer_vs_player():
    global board
    board = [str(i+1) for i in range(9)]  # Reset board to numbered positions
    while True:
        show_board()
        if count_board('X') == count_board('O'):
            print("Player X, make a selection:")
            get_player_choice('X')
        else:
            get_computer_choice()
        
        winner = check_winner()
        if winner in ('X', 'O'):
            show_board()
            print(f"{winner} won!! GameOver")
            break
        elif winner == 'D':
            show_board()
            print("It is a tie!!")
            break

def player_vs_player():
    global board
    board = [str(i+1) for i in range(9)]
    while True:
        show_board()
        if count_board('X') == count_board('O'):
            print("Player X, make a selection:")
            get_player_choice('X')
        else:
            print("Player O, make a selection:")
            get_player_choice('O')

        winner = check_winner()
        if winner in ('X', 'O'):
            show_board()
            print(f"{winner} won!! GameOver")
            break
        elif winner == 'D':
            show_board()
            print("It is a tie!!")
            break

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Single Player")
        print("2. Multiplayer")
        print("3. Exit Game")
        mode = input("Select an option: ").strip()
        
        if mode == '1':
            computer_vs_player()
        elif mode == '2':
            player_vs_player()
        elif mode == '3':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input! Please select 1, 2, or 3.")

if __name__ == "__main__":
    print("##################################")
    print("#   Welcome to TicTacToe Game!   #")
    print("##################################\n")
    main_menu()
