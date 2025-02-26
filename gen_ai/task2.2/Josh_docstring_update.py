# Tic Tac Toe game

import random

def show_board():
    """
    Displays the current state of the Tic Tac Toe board.
    """
    print("\n ----------- ")
    for i in range(0, 9, 3):
        print(f"| {board[i]} | {board[i+1]} | {board[i+2]} |")
        print(" ----------- ")

def count_board(symbol):
    """
    Counts the occurrences of a given symbol ('X' or 'O') on the board.
    
    Parameters:
        symbol (str): The symbol to count ('X' or 'O').
    
    Returns:
        int: Number of times the symbol appears on the board.
    """
    return board.count(symbol)

def check_winner():
    """
    Checks the board for a winner or a tie.
    
    Returns:
        str: 'X' or 'O' if there is a winner, 'D' if it's a draw, 'C' if the game continues.
    """
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] in ('X', 'O'):
            return board[a]
    
    return 'D' if all(cell in ('X', 'O') for cell in board) else 'C'

def get_player_choice(symbol):
    """
    Prompts the player to enter their move and updates the board.
    
    Parameters:
        symbol (str): The player's symbol ('X' or 'O').
    """
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
    """
    Determines and makes the best possible move for the computer ('O').
    
    The strategy follows:
    - Win if possible in this move.
    - Block the player from winning in the next move.
    - Choose the best available move based on priority (center, corners, edges).
    """
    best_moves = [4, 0, 2, 6, 8, 1, 3, 5, 7]  # Prioritized positions

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
    """
    Runs a single-player game where the player ('X') competes against the computer ('O').
    """
    global board
    board = [str(i+1) for i in range(9)]  # Initialize board
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
            print(f"{winner} won!! Game Over")
            break
        elif winner == 'D':
            show_board()
            print("It is a tie!!")
            break

def player_vs_player():
    """
    Runs a two-player game where 'X' and 'O' take turns.
    """
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
            print(f"{winner} won!! Game Over")
            break
        elif winner == 'D':
            show_board()
            print("It is a tie!!")
            break

def main_menu():
    """
    Displays the main menu and handles user selection.
    """
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
