import tkinter as tk
import Reversi
from tkinter import messagebox

"""    
Implementation of the Reversi GUI incoorporating the Game Logic (Normal Reversi with NO AI)
"""

class ReversiHuman:
    def __init__(self, master):
        self.master = master
        self.master.title("Reversi")

        # Create a frame to hold the game board and counts
        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)  # Add some padding
        
        # Create the canvas for the game board
        self.canvas = tk.Canvas(self.frame, width=400, height=400, bg="green")
        self.canvas.grid(row=0, column=0)  # Place canvas in the first row and column
        
        # Create a frame to hold the piece counts
        self.count_frame = tk.Frame(self.frame)
        self.count_frame.grid(row=1, column=0, pady=10)  # Place counts below the canvas

        # Initialize the game
        self.reversi = Reversi.Reversi()

        # Draw board
        self.draw_board()

        # Draw counts
        self.white_count_label = tk.Label(self.count_frame, text="White: 2", fg="white", bg="green")
        self.white_count_label.pack(side="left", padx=10)  # Add some padding
        self.black_count_label = tk.Label(self.count_frame, text="Black: 2", fg="black", bg="green")
        self.black_count_label.pack(side="right", padx=10)  # Add some padding

        # Bind mouse click event
        self.canvas.bind("<Button-1>", self.on_click)

        # Print the initial board state
        print("\nInitial Board State:")
        self.reversi.print_board()

        # Generate possible moves for the white player 
        possible_moves_white = self.reversi.generate_possible_moves(self.reversi.white)
        print("\nPossible Moves for White Player:", possible_moves_white)

        # Generate possible moves for the black player
        possible_moves_black = self.reversi.generate_possible_moves(self.reversi.black)
        print("Possible Moves for Black Player:", possible_moves_black)

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                x0, y0 = i * 50, j * 50
                x1, y1 = x0 + 50, y0 + 50
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="green")

        # Draw valid move indicators for the current player's turn
        if not self.reversi.is_terminal_state():
            current_player_moves = self.reversi.generate_possible_moves(self.reversi.current_player)
            for move in current_player_moves:
                row, col = move
                x, y = col * 50 + 25, row * 50 + 25
                if self.reversi.current_player == self.reversi.white:
                    self.canvas.create_line(x - 15, y - 15, x + 15, y + 15, width=2, fill="white")
                    self.canvas.create_line(x - 15, y - 15, x + 15, y + 15, width=2, fill="white")
                else:
                    self.canvas.create_line(x - 15, y - 15, x + 15, y + 15, width=2, fill="black")
                    self.canvas.create_line(x + 15, y - 15, x - 15, y + 15, width=2, fill="black")

        # Draw existing pieces
        for row in range(8):
            for col in range(8):
                if self.reversi.board[row][col] == 1:
                    self.draw_piece(row, col, "white")
                elif self.reversi.board[row][col] == 2:
                    self.draw_piece(row, col, "black")

    def draw_piece(self, row, col, color):
        x, y = col * 50 + 25, row * 50 + 25
        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=color)

    def update_counts(self):
        white_count = sum(row.count(1) for row in self.reversi.board)
        black_count = sum(row.count(2) for row in self.reversi.board)
        self.white_count_label.config(text=f"White: {white_count}")
        self.black_count_label.config(text=f"Black: {black_count}")

    def on_click(self, event):
        if not self.reversi.is_terminal_state():  # Check if the game is not in a terminal state
            row, col = event.y // 50, event.x // 50
            if (row, col) in self.reversi.generate_possible_moves(self.reversi.current_player):
                self.reversi.make_move(row, col)
                self.update_board()

    def update_board(self):
        self.canvas.delete("all")
        self.draw_board()
        self.update_counts() 

        if self.reversi.is_terminal_state():
            winner = self.reversi.calculate_winner()
            if winner == 0:
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")

def main():
    root = tk.Tk()
    ReversiHuman(root)
    root.mainloop()

if __name__ == "__main__":
    main()

