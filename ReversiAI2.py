import tkinter as tk
from tkinter import messagebox
import Reversi
from AlphaBeta import AlphaBetaPlayer
from HeuristicEvaluator import HeuristicEvaluator

class ReversiAI2:
    def __init__(self, master):
        self.master = master
        self.master.title("Reversi AI")

        self.frame = tk.Frame(master)
        self.frame.pack(padx=20, pady=20)
        
        self.canvas = tk.Canvas(self.frame, width=400, height=400, bg="green")
        self.canvas.grid(row=0, column=0)

        self.count_frame = tk.Frame(self.frame)
        self.count_frame.grid(row=1, column=0, pady=10)

        self.reversi = Reversi.Reversi()
        self.reversi.current_player = self.reversi.white  # AI (white) starts first

        heuristic_evaluator = HeuristicEvaluator(player_color=1)  # AI is white
        self.ai_player = AlphaBetaPlayer(player_color=1, max_depth=4, 
                                         heuristic_strategy=heuristic_evaluator.heuristic_strategy_1, 
                                         strategies=[heuristic_evaluator.heuristic_strategy_1, heuristic_evaluator.heuristic_strategy_3])

        self.draw_board()
        self.update_counts()

        self.master.after(500, self.ai_move)  # Schedule the AI's first move
        self.canvas.bind("<Button-1>", self.on_click)  # Bind mouse click for human moves

    def draw_board(self):
        print("Redrawing board:")  # Log message to indicate board redraw
        self.canvas.delete("all")  # Clear the canvas before redrawing
        for i in range(8):
            row_display = []
            for j in range(8):
                x0, y0 = j * 50, i * 50
                x1, y1 = x0 + 50, y0 + 50
                self.canvas.create_rectangle(x0, y0, x1, y1, outline="black", fill="green")  # Draw each board square

                # Check if the square contains a piece and draw it
                piece = self.reversi.board[i][j]
                if piece != 0:
                    color = "white" if piece == 1 else "black"
                    self.draw_piece(i, j, color)
                    row_display.append(color[0].upper())  # Append 'W' for white, 'B' for black
                else:
                    row_display.append('-')  # Append '-' for empty

            print(" ".join(row_display))  # Print the current row's state

        # Draw valid moves for the current player with crosses
        self.draw_valid_moves()

    def draw_valid_moves(self):
        # Get valid moves for the current player
        valid_moves = self.reversi.generate_possible_moves(self.reversi.current_player)
        for move in valid_moves:
            row, col = move
            x, y = col * 50 + 25, row * 50 + 25
            if self.reversi.current_player == self.reversi.white:
                # Draw a white cross for valid white moves
                self.canvas.create_line(x - 10, y - 10, x + 10, y + 10, fill="white", width=2)
                self.canvas.create_line(x + 10, y - 10, x - 10, y + 10, fill="white", width=2)
            else:
                # Draw a black cross for valid black moves
                self.canvas.create_line(x - 10, y - 10, x + 10, y + 10, fill="black", width=2)
                self.canvas.create_line(x + 10, y - 10, x - 10, y + 10, fill="black", width=2)


    def draw_piece(self, row, col, color):
        x, y = col * 50 + 25, row * 50 + 25
        self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill=color)

    def update_counts(self):
        white_count = sum(row.count(1) for row in self.reversi.board)
        black_count = sum(row.count(2) for row in self.reversi.board)

    def on_click(self, event):
        if not self.reversi.is_terminal_state() and self.reversi.current_player == self.reversi.black:
            row, col = event.y // 50, event.x // 50
            if (row, col) in self.reversi.generate_possible_moves(self.reversi.current_player):
                self.reversi.make_move(row, col)
                self.update_board()
                if not self.reversi.is_terminal_state():
                    self.master.after(500, self.ai_move)  # Schedule AI move after human move

    def ai_move(self):
        # Check if the game has reached a terminal state, which would mean no further moves are possible.
        if self.reversi.is_terminal_state():
            print("Game has reached a terminal state; no further moves possible.")
        else:
            print("Game continues; checking for AI's turn...")

        # Check if it is currently the AI's turn (AI is white player).
        if self.reversi.current_player != self.reversi.white:
            print("It is not AI's turn, current player is not white.")
        else:
            print("It is the AI's turn (white).")
        
        # Only proceed if it's not a terminal state and it's the AI's turn.
        if not self.reversi.is_terminal_state() and self.reversi.current_player == self.reversi.white:
            print("Preparing to calculate the best move for AI.")
            
            # The AI calculates its best move based on the current state of the board.
            move = self.ai_player.get_best_move(self.reversi)
            
            # Print the move the AI has decided to make
            print(f"AI move calculated: {move}")

            # Check if a valid move was returned by the AI.
            if move:
                print("AI has a valid move, executing move...")
                
                # If a valid move is available, make that move on the board.
                self.reversi.make_move(*move)
                
                # Update the board and refresh UI elements accordingly.
                self.update_board()
                print("Board updated after AI move.")
            else:
                # If no valid move is available, it might indicate a blocked board or an error in logic.
                print("No valid move for AI.")
        else:
            print("Skipping AI move due to game state or turn condition.")


    def update_board(self):
        self.canvas.delete("all")
        self.draw_board()
        self.update_counts()
        if self.reversi.is_terminal_state():
            winner = self.reversi.calculate_winner()
            message = "It's a draw!" if winner == 0 else f"Player {winner} wins!"
            messagebox.showinfo("Game Over", message)
        print("Board updated")  # Confirm the board updates


def main():
    root = tk.Tk()
    ReversiAI2(root)
    root.mainloop()

if __name__ == "__main__":
    main()