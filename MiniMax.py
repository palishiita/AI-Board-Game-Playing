import copy

class MiniMaxPlayer:
    """
    player_color: The color of the player (1 for white, 2 for black).
    max_depth: The maximum depth to search in the game tree during minimax algorithm.
    heuristic_strategy: The heuristic function used to evaluate game states
    """
    def __init__(self, player_color, max_depth, heuristic_strategy):
        self.player_color = player_color
        self.max_depth = max_depth
        self.heuristic_strategy = heuristic_strategy

    def make_move(self):
        """
        Makes a move by performing the MiniMax search and selecting the best move.
        """
        _, move = self.maximize(copy.deepcopy(self.game), self.max_depth, float('-inf'), float('inf'))
        return move

    def maximize(self, game, depth, alpha, beta):
        """
        Maximizes the score for the current player.
        
        Parameters:
        - game: The current game state.
        - depth: The current depth in the game tree.
        - alpha: The best score achievable by the maximizing player.
        - beta: The best score achievable by the minimizing player.
        
        Returns:
        - The maximum score achievable by the current player.
        - The best move corresponding to the maximum score.
        """
        if depth == 0 or game.is_terminal_state():
            # If at maximum depth or terminal state, return heuristic score
            return self.heuristic_strategy(game), None

        max_score = float('-inf')
        best_move = None

        for move in game.get_valid_moves(self.player_color):
            # For each valid move for the current player
            game_copy = copy.deepcopy(game)  # Make a copy of the game state
            game_copy.make_move(*move)  # Apply the move to the copied game state
            # Recursively minimize the opponent's score
            score, _ = self.minimize(game_copy, depth - 1, alpha, beta)
            if score > max_score:
                # Update maximum score and corresponding move if a better move is found
                max_score = score
                best_move = move
            alpha = max(alpha, max_score)  # Update alpha value
            if alpha >= beta:
                # Beta pruning: stop searching if maximum score exceeds minimum score
                break
        return max_score, best_move

    def minimize(self, game, depth, alpha, beta):
        """
        Minimizes the score for the opponent player.
        
        Parameters:
        - game: The current game state.
        - depth: The current depth in the game tree.
        - alpha: The best score achievable by the maximizing player.
        - beta: The best score achievable by the minimizing player.
        
        Returns:
        - The minimum score achievable by the opponent player.
        - The best move corresponding to the minimum score.
        """
        if depth == 0 or game.is_terminal_state():
            # If at maximum depth or terminal state, return heuristic score
            return self.heuristic_strategy(game), None

        min_score = float('inf')
        best_move = None

        for move in game.get_valid_moves(3 - self.player_color):
            # For each valid move for the opponent player
            game_copy = copy.deepcopy(game)  # Make a copy of the game state
            game_copy.make_move(*move)  # Apply the move to the copied game state
            # Recursively maximize the current player's score
            score, _ = self.maximize(game_copy, depth - 1, alpha, beta)
            if score < min_score:
                # Update minimum score and corresponding move if a better move is found
                min_score = score
                best_move = move
            beta = min(beta, min_score)  # Update beta value
            if beta <= alpha:
                # Alpha pruning: stop searching if minimum score falls below maximum score
                break
        return min_score, best_move
