def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        row, col = -1, -1

        while True:
            try:
                row, col = map(int, input(f"Player {players[turn]}, enter row and column (0-2): ").split())
                if board[row][col] == " ":
                    break
                else:
                    print("Spot already taken! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Enter two numbers between 0 and 2.")

        board[row][col] = players[turn]

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        turn = 1 - turn  # Switch players

if __name__ == "__main__":
    tic_tac_toe()



#Commented version
def print_board(board):
    """Prints the Tic-Tac-Toe board in a formatted way."""
    for row in board:
        print(" | ".join(row))  # Print the row with separators
        print("-" * 9)  # Print a horizontal line to separate rows

def check_winner(board):
    """Checks if there is a winner in the current board state."""
    # Check rows and columns for a winning line
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":  # Check row
            return board[i][0]  # Return the winning symbol
        if board[0][i] == board[1][i] == board[2][i] != " ":  # Check column
            return board[0][i]  # Return the winning symbol

    # Check diagonals for a winning line
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]  # Return the winning symbol (left-to-right diagonal)
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]  # Return the winning symbol (right-to-left diagonal)

    return None  # No winner found

def is_full(board):
    """Returns True if the board is full (no empty spaces left), otherwise False."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game."""
    # Initialize a 3x3 board filled with empty spaces
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]  # Players take turns using "X" and "O"
    turn = 0  # Player index (0 for "X", 1 for "O")

    while True:
        print_board(board)  # Display the current board state
        row, col = -1, -1  # Initialize row and column for player input

        # Get a valid move from the player
        while True:
            try:
                row, col = map(int, input(f"Player {players[turn]}, enter row and column (0-2): ").split())
                if board[row][col] == " ":  # Check if the selected cell is empty
                    break  # Valid move, exit loop
                else:
                    print("Spot already taken! Try again.")
            except (ValueError, IndexError):  # Handle invalid input
                print("Invalid input! Enter two numbers between 0 and 2.")

        board[row][col] = players[turn]  # Place the player's symbol on the board

        # Check if the current player has won
        winner = check_winner(board)
        if winner:
            print_board(board)  # Show final board state
            print(f"Player {winner} wins!")  # Announce the winner
            break  # End the game

        # Check if the board is full (tie)
        if is_full(board):
            print_board(board)  # Show final board state
            print("It's a tie!")  # Announce the tie
            break  # End the game

        turn = 1 - turn  # Switch player turn (0 -> 1, 1 -> 0)

if __name__ == "__main__":
    tic_tac_toe()  # Start the game if this script is run directly

