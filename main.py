import tkinter as tk 
from tkinter import messagebox 


# Function to check if a player has won
def check_winner(board, player):
    # Check rows for a win
    for row in board:
        if all(cell["text"] == player for cell in row):  
            return True

    # Check columns for a win
    for col in range(3):
        if all(board[row][col]["text"] == player for row in range(3)): 
            return True

    # Check diagonals for a win
    if all(board[i][i]["text"] == player for i in range(3)) or all(board[i][2 - i]["text"] == player for i in range(3)):
        return True 

    return False  # no winner yet


# Tie game function
def is_full(board):
    return all(cell["text"] != "" for row in board for cell in row)  

def on_click(row, col):
    global turn, board 
    player = players[turn % 2] 

    if board[row][col]["text"] == "":  
        board[row][col]["text"] = player 

        # Check if this move wins the game
        if check_winner(board, player):
            messagebox.showinfo("Game Over", f"Player {player} wins!")  
            reset_board()  
            return
            
        if is_full(board):
            messagebox.showinfo("Game Over", "It's a tie!")  # Show tie message
            reset_board()
            return

        turn += 1 


def reset_board():
    global board, turn 
    turn = 0 
    for row in board:
        for cell in row:
            cell["text"] = ""  



def create_gui():
    global board, players, turn  

    root = tk.Tk()  
    root.title("Tic-Tac-Toe")  

    players = ["X", "O"]  
    turn = 0 
    board = [[None for _ in range(3)] for _ in range(3)]  


    for row in range(3):
        for col in range(3):
            cell = tk.Button(root, text="", font=("Gotham", 24), width=5, height=2,
                             command=lambda r=row, c=col: on_click(r, c)) 
            cell.grid(row=row, column=col) 
            board[row][col] = cell  

    root.mainloop() 


if __name__ == "__main__":
    create_gui() 

