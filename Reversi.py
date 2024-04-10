"""    
Task 1: 
Defining the board state and a function that generates possible moves from a given board state.
"""

class Reversi:

    def __init__(self):
        # Initialize the board with an 8x8 grid
        self.board = [[0] * 8 for _ in range(8)]

        # Initialize the starting pieces in the center of the board
        self.board[3][3] = self.board[4][4] = 1  # White pieces
        self.board[3][4] = self.board[4][3] = 2  # Black pieces

        # Define player colors
        self.white = 1
        self.black = 2

    def print_board(self):
        # Print the current state of the board
        for row in self.board:
            print(' '.join(map(str, row)))

    def get_valid_moves(self, player, row=None, col=None):
        valid_moves = []

        if row is not None and col is not None:
            # Check if the specified position is a valid move
            if self.is_valid_move(row, col, player):
                valid_moves.append((row, col))
            return valid_moves

        # Iterate through each cell on the board
        for i in range(8):
            for j in range(8):
                # Check if the cell is empty
                if self.board[i][j] == 0:
                    # Check if the move is valid by checking all 8 directions
                    if self.is_valid_move(i, j, player):
                        valid_moves.append((i, j))

        return valid_moves


    def is_valid_move(self, row, col, player):
        # Check if the move is valid in any direction
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                # Skip the current cell and out-of-bounds cells
                if dr == dc == 0 or not (0 <= row + dr < 8 and 0 <= col + dc < 8):
                    continue

                # Check if there is an opponent's piece in this direction
                if self.has_opponent_piece(row, col, player, dr, dc):
                    # Check if the move would result in flipping opponent's pieces
                    if self.can_flip_pieces(row, col, player, dr, dc):
                        return True

        return False

    def has_opponent_piece(self, row, col, player, dr, dc):
        opponent = self.black if player == self.white else self.white
        return 0 <= row + dr < 8 and 0 <= col + dc < 8 and self.board[row + dr][col + dc] == opponent

    def can_flip_pieces(self, row, col, player, dr, dc):
        opponent = self.black if player == self.white else self.white
        r, c = row + dr, col + dc

        while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == opponent:
            r += dr
            c += dc

        return 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == player

    def set_board_from_input(self, input_lines):
        for i in range(8):
            for j in range(8):
                self.board[i][j] = int(input_lines[i][j])

  

# Create an instance of the Reversi game
game = Reversi()

# Accept input in the form of 8 linesof numbers
# Default initial board state
default_input = [
    "0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0",
    "0 0 0 1 2 0 0 0",
    "0 0 0 2 1 0 0 0",
    "0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0",
    "0 0 0 0 0 0 0 0"
]

# Assign default initial board state to input_lines
input_lines = [line.split() for line in default_input]


# Set the board state from the input
game.set_board_from_input(input_lines)

# # Print the initial board state
print("\nInitial Board State:")
game.print_board()

def task1():
    # Get valid moves for the white player 
    valid_moves_white = game.get_valid_moves(game.white)
    print("\nValid Moves for White Player:", valid_moves_white)

    # Get valid moves for the black player
    valid_moves_black = game.get_valid_moves(game.black)
    print("Valid Moves for Black Player:", valid_moves_black)

task1()