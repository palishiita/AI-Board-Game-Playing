import tkinter as tk
import Reversi
from tkinter import messagebox
from AlphaBeta import AlphaBetaPlayer
from HeuristicEvaluator import HeuristicEvaluator


"""    
Implementation of the Reversi GUI incoorporating the Game Logic and AI
"""

class ReversiAI:
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

        # Create heuristic evaluators for each player
        player1_strategies = [HeuristicEvaluator(player_color=1).heuristic_strategy_1,
                              HeuristicEvaluator(player_color=1).heuristic_strategy_3,
                              HeuristicEvaluator(player_color=1).heuristic_strategy_5]

        player2_strategies = [HeuristicEvaluator(player_color=2).heuristic_strategy_2,
                              HeuristicEvaluator(player_color=2).heuristic_strategy_4,
                              HeuristicEvaluator(player_color=2).heuristic_strategy_6]


        # Create AlphaBetaPlayers for each player
        self.player1 = AlphaBetaPlayer(player_color=1, max_depth=4, heuristic_strategy=HeuristicEvaluator(player_color=1).heuristic_strategy_1, strategies=player1_strategies)
        self.player2 = AlphaBetaPlayer(player_color=2, max_depth=4, heuristic_strategy=HeuristicEvaluator(player_color=2).heuristic_strategy_2, strategies=player2_strategies)

        # Draw board
        self.draw_board()

        # Draw counts
        self.white_count_label = tk.Label(self.count_frame, text="White: 2", fg="white", bg="green")
        self.white_count_label.pack(side="left", padx=10)  # Add some padding
        self.black_count_label = tk.Label(self.count_frame, text="Black: 2", fg="black", bg="green")
        self.black_count_label.pack(side="right", padx=10)  # Add some padding

        # Start the game loop
        self.play_game()

    def draw_board(self):
        self.canvas.delete("pieces")  # Clear the canvas before drawing
        for row in range(8):
            for col in range(8):
                x0, y0 = col * 50, row * 50
                x1, y1 = x0 + 50, y0 + 50
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="green")

                if self.reversi.board[row][col] == 1:
                    self.draw_piece(row, col, "white")
                elif self.reversi.board[row][col] == 2:
                    self.draw_piece(row, col, "black")

    def draw_piece(self, row, col, color):
        x, y = col * 50 + 25, row * 50 + 25
        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=color, tags="pieces")

    def update_counts(self):
        white_count = sum(row.count(1) for row in self.reversi.board)
        black_count = sum(row.count(2) for row in self.reversi.board)
        self.white_count_label.config(text=f"White: {white_count}")
        self.black_count_label.config(text=f"Black: {black_count}")

    def update_board(self):
        self.update_counts()
        self.draw_board()
        self.master.update()  # Update the tkinter window

    def play_game(self):
        while not self.reversi.is_terminal_state():
            if self.reversi.current_player == self.reversi.white:
                move = self.player1.get_best_move(self.reversi)
            else:
                move = self.player2.get_best_move(self.reversi)
                
            if move:
                self.reversi.make_move(*move)
                self.update_board()

        # Game over, show result
        winner = self.reversi.calculate_winner()
        if winner == 0:
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")

def main():
    root = tk.Tk()
    ReversiAI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
