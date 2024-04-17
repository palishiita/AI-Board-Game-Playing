"""    
Implementation of the Reversi Game Logic based on its rules.
"""
class Reversi:
    def __init__(self):
        self.board = [[0] * 8 for _ in range(8)]
        self.board[3][3] = self.board[4][4] = 1  # White pieces
        self.board[3][4] = self.board[4][3] = 2  # Black pieces
        self.white = 1
        self.black = 2
        self.current_player = self.black

    def print_board(self):
        for row in self.board:
            print(' '.join(map(str, row)))

    def generate_possible_moves(self, player):
        possible_moves = []
    
        # Iterate over each cell on the game board
        for row in range(8):
            for col in range(8):
                # Check if the cell is empty and the move is valid for the specified player
                if self.board[row][col] == 0 and self.is_valid_move(row, col, player):
                    # If the conditions are met, append the coordinates of the cell to the list of possible moves
                    possible_moves.append((row, col))
    
        return possible_moves

    def is_valid_move(self, row, col, player):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        opponent = self.white if player == self.black else self.black

        if self.board[row][col] != 0:
            return False

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                r += dr
                c += dc
                while 0 <= r < 8 and 0 <= c < 8:
                    if self.board[r][c] == 0:
                        break
                    elif self.board[r][c] == player:
                        return True
                    r += dr
                    c += dc

        return False

    def make_move(self, row, col):
        # Determine the opponent's color based on the current player
        opponent = self.white if self.current_player == self.black else self.black
        
        # Place the current player's piece at the specified row and column
        self.board[row][col] = self.current_player
        
        # Define the directions in which to search for opponent's pieces
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    
        # Iterate over each direction to check for opponent's pieces to flip
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
                r += dr
                c += dc
                # Continue in the direction until reaching an empty cell or the board boundary
                while 0 <= r < 8 and 0 <= c < 8:
                    if self.board[r][c] == 0:
                        break  # Stop if an empty cell is encountered
                    elif self.board[r][c] == self.current_player:
                        # If the current player's piece is found, flip opponent's pieces in between
                        r_back, c_back = row + dr, col + dc
                        while (r_back, c_back) != (r, c):
                            self.board[r_back][c_back] = self.current_player
                            r_back += dr
                            c_back += dc
                        break
                    r += dr
                    c += dc
    
        # Switch to the next player's turn
        self.current_player = self.white if self.current_player == self.black else self.black

    def get_valid_moves(self, player):
        valid_moves = []

        for row in range(8):
            for col in range(8):
                if self.board[row][col] == 0 and self.is_valid_move(row, col, player):
                    valid_moves.append((row, col))

        return valid_moves

    def is_terminal_state(self):
        # Check if the current player has no valid moves
        if not self.get_valid_moves(self.current_player):
            # Switch player and check if the other player also has no valid moves
            self.current_player = self.white if self.current_player == self.black else self.black
            if not self.get_valid_moves(self.current_player):
                return True  # Both players have no valid moves, game is over
        return False  # Game is not over yet

    def calculate_winner(self):
        player1_pieces = sum(row.count(1) for row in self.board)
        player2_pieces = sum(row.count(2) for row in self.board)

        if player1_pieces > player2_pieces:
            return 1  # Player 1 (white) wins
        elif player2_pieces > player1_pieces:
            return 2  # Player 2 (black) wins
        else:
            return 0  # It's a draw
