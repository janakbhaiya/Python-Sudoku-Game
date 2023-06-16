import numpy as np

# Function to print the Sudoku board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Function to check if the Sudoku board is full
def is_board_full(board):
    for row in board:
        if 0 in row:
            return False
    return True

# Function to check if a number is valid in a given position
def is_valid_move(board, num, row, col):
    # Check if the number already exists in the row
    if num in board[row]:
        return False

    # Check if the number already exists in the column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number already exists in the 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, num, row, col):
                        board[row][col] = num

                        if solve_sudoku(board):
                            return True

                        board[row][col] = 0

                return False

    return True

# Initialize an empty Sudoku board
board = np.zeros((9, 9), dtype=int)

# Main game loop
while True:
    print("\n--- Sudoku Game ---")
    print("1. New Game")
    print("2. Quit")
    print("3. Continue")
    print("4. Pause")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Start a new game
        board = np.zeros((9, 9), dtype=int)
        solve_sudoku(board)
        print("\nNew game started. Enjoy!")

    elif choice == "2":
        # Quit the game
        print("Goodbye!")
        break

    elif choice == "3":
        # Continue the current game
        if is_board_full(board):
            print("Congratulations! You have solved the Sudoku.")
        else:
            print("\nCurrent Sudoku board:")
            print_board(board)

    elif choice == "4":
        # Pause the game
        print("Game paused. You can resume later.")

    else:
        print("Invalid choice. Please try again.")