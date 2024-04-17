# AI BOARD GAME REVERSI

![Alt text](image.png)


## Background about Reversi

**Here are the rules of Reversi:**

- Starting Position: The game starts with four discs placed in the center of the board in a pattern of two black discs and two white discs, arranged diagonally with same-colored discs facing each other.

- Turns: Players take turns placing one disc of their color on an empty square on the board. Black always plays first.

- Legal Moves: A move is legal if and only if it results in at least one of the opponent's discs being flipped (changed to the current player's color) along a straight line (horizontally, vertically, or diagonally) between the newly placed disc and another disc of the current player's color. This means that at least one of the opponent's discs must be sandwiched between the newly placed disc and another disc of the current player's color.

- Flipping: When a player makes a legal move and flips one or more of the opponent's discs, all of the flipped discs are turned to the current player's color.

- End of the Game: The game ends when either:
i) Both players have no legal moves left.
ii) The board is full.

- Winning: The player with the most discs of their color on the board at the end of the game wins. It's possible for the game to end in a tie if both players have the same number of discs.

## Heuristic Evaluator
### Heuristic Strategy 1: Coin Parity
- **Description**: Calculates the difference between the number of disks of the player's color and the opponent's color.
- **Formula**: `max_score - min_score`, where `max_score` is the total number of player's disks and `min_score` is the total number of opponent's disks.
- **Advantage**: Encourages the player to aim for having more disks than the opponent on the board.
- **Disadvantage**: Ignores other important factors like mobility and positional advantage.

### Heuristic Strategy 2: Mobility
- **Description**: Computes the difference between the number of valid moves available to the player and the opponent.
- **Formula**: `max_mobility - min_mobility`, where `max_mobility` is the number of valid moves for the player and `min_mobility` is the number of valid moves for the opponent.
- **Advantage**: Promotes actions that increase the player's mobility, allowing for more strategic options.
- **Disadvantage**: Doesn't consider the quality of the moves or positional advantage.

### Heuristic Strategy 3: Mobility and Corners
- **Description**: Combines the evaluation of mobility with the control of corner positions.
- **Formula**: `(max_mobility + max_corners) - (min_mobility + min_corners)`, where `max_corners` is the number of corners controlled by the player and `min_corners` is the number of corners controlled by the opponent.
- **Advantage**: Rewards the player for controlling corner positions, which are strategically valuable in Reversi.
- **Disadvantage**: Still overlooks other aspects like edge control and disk stability.

### Heuristic Strategy 4: Mobility and Stability
- **Description**: Integrates mobility with disk stability, where stability refers to the number of stable disks on the board.
- **Formula**: `(max_mobility + max_stability) - (min_mobility + min_stability)`, where `max_stability` is the number of stable disks for the player and `min_stability` is the number of stable disks for the opponent.
- **Advantage**: Encourages the player to create stable positions, which are less likely to be flipped by the opponent.
- **Disadvantage**: May not prioritize immediate board control or strategic positions.

### Heuristic Strategy 5: Mobility, Corners, and Edges
- **Description**: Extends the evaluation to include edge control along with mobility and corners.
- **Formula**: `(max_mobility + max_corners + max_edges) - (min_mobility + min_corners + min_edges)`, where `max_edges` is the number of edges controlled by the player and `min_edges` is the number of edges controlled by the opponent.
- **Advantage**: Recognizes the importance of controlling edges, which can limit opponent's mobility and provide positional advantage.
- **Disadvantage**: Complexity increases with more factors considered, potentially leading to longer evaluation times.

### Heuristic Strategy 6: Mobility, Corners, Edges, and Stability
- **Description**: Integrates all previously mentioned factors: mobility, corners, edges, and disk stability.
- **Formula**: `(max_mobility + max_corners + max_edges + max_stability) - (min_mobility + min_corners + min_edges + min_stability)`.
- **Advantage**: Provides a comprehensive evaluation considering various strategic elements of the game.
- **Disadvantage**: Increased computational complexity due to the combination of multiple factors, potentially leading to slower decision-making.


## Min Max Algorithm

**MiniMax Class**
- **Purpose**: Implements the MiniMax algorithm for decision-making in the game of Reversi/Othello.
- **Initialization**: Initializes the MiniMax player with parameters such as player color, maximum search depth, and a heuristic strategy for evaluating game states.
- **Functionality**:
  - `make_move`: Determines the best move for the player using MiniMax algorithm up to the specified depth.
  - `maximize` and `minimize`: Recursive functions for exploring game tree, maximizing player's score and minimizing opponent's score, respectively.

## Alpha Beta Prunning

**AlphaBetaPlayer Class**
- **Purpose**: Extends `MiniMaxPlayer` to implement the Alpha-Beta Pruning algorithm, optimizing the search process.
- **Initialization**: Inherits parameters from `MiniMaxPlayer` and adds a list of heuristic strategies.
- **Functionality**:
  - `get_best_move`: Overrides `make_move` to find the best move using Alpha-Beta algorithm.
  - `max_value` and `min_value`: Implement Alpha-Beta pruning for maximizing efficiency.
  - `evaluate`: Evaluates the current game state using a specified heuristic strategy.


## Reversi AI
- **Purpose**: Implements the Reversi game GUI incorporating game logic and AI players.
- **Initialization**: Sets up the tkinter window and frames for the game board and piece counts. Initializes the game, heuristic evaluators, and AlphaBetaPlayers for both players.
- **Functionality**:
  - `draw_board`: Draws the game board on the canvas using rectangles and fills them with pieces if present.
  - `draw_piece`: Draws a piece (white or black) at the specified row and column.
  - `update_counts`: Updates and displays the count of white and black pieces.
  - `update_board`: Updates the board and counts after each move.
  - `play_game`: Manages the game loop where players take turns to make moves until the game ends.
 
For both the `AlphaBetaPlayer` Class and `MiniMax` Class deep copy was used. Enables deep copying of game states to ensure the original game state remains unchanged during search. Utilizes the `copy.deepcopy` function to create copies of game states before making and evaluating potential moves.
