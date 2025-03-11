import tkinter as tk  # Import tkinter for GUI
from tkinter import messagebox  # Import messagebox to show pop-up alerts


# Function to check if a player has won
def check_winner(board, player):
    # Check rows for a win
    for row in board:
        if all(cell["text"] == player for cell in row):  # If all cells in a row match the player
            return True

    # Check columns for a win
    for col in range(3):
        if all(board[row][col]["text"] == player for row in range(3)):  # If all cells in a column match
            return True

    # Check diagonals for a win
    if all(board[i][i]["text"] == player for i in range(3)) or all(board[i][2 - i]["text"] == player for i in range(3)):
        return True  # If all cells in either diagonal match

    return False  # No winner yet


# Function to check if the board is full (tie game)
def is_full(board):
    return all(cell["text"] != "" for row in board for cell in row)  # If no empty cells remain


# Function to handle a button click
def on_click(row, col):
    global turn, board  # Access global variables
    player = players[turn % 2]  # Determine whose turn it is ("X" or "O")

    if board[row][col]["text"] == "":  # Check if the cell is empty
        board[row][col]["text"] = player  # Mark the cell with the player's symbol

        # Check if this move wins the game
        if check_winner(board, player):
            messagebox.showinfo("Game Over", f"Player {player} wins!")  # Show winner message
            reset_board()  # Reset the game board
            return

        # Check if the game is a tie
        if is_full(board):
            messagebox.showinfo("Game Over", "It's a tie!")  # Show tie message
            reset_board()  # Reset the game board
            return

        turn += 1  # Move to the next turn


# Function to reset the board
def reset_board():
    global board, turn  # Access global variables
    turn = 0  # Reset turn counter
    for row in board:
        for cell in row:
            cell["text"] = ""  # Clear all cells


# Function to create the GUI window and board
def create_gui():
    global board, players, turn  # Access global variables

    root = tk.Tk()  # Create the main Tkinter window
    root.title("Tic-Tac-Toe")  # Set window title

    players = ["X", "O"]  # Define player symbols
    turn = 0  # Start with player "X"
    board = [[None for _ in range(3)] for _ in range(3)]  # Create a 3x3 board

    # Create 3x3 grid of buttons
    for row in range(3):
        for col in range(3):
            cell = tk.Button(root, text="", font=("Gotham", 24), width=5, height=2,
                             command=lambda r=row, c=col: on_click(r, c))  # Button click calls on_click()
            cell.grid(row=row, column=col)  # Place button in the grid
            board[row][col] = cell  # Store button in the board

    root.mainloop()  # Run the Tkinter event loop


# Run the game
if __name__ == "__main__":
    create_gui()  # Start the GUI
