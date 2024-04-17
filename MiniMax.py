import copy

"""

"""

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
        _, move = self.maximize(copy.deepcopy(self.game), self.max_depth, float('-inf'), float('inf'))
        return move

    """
    game: The current game state.
    depth: The current depth in the game tree.
    alpha: The best score that the maximizing player can achieve.
    beta: The best score that the minimizing player can achieve.
    """
    def maximize(self, game, depth, alpha, beta):
        if depth == 0 or game.is_terminal_state():
            return self.heuristic_strategy(game), None

        max_score = float('-inf')
        best_move = None

        for move in game.get_valid_moves(self.player_color):
            game_copy = copy.deepcopy(game)
            game_copy.make_move(*move)
            score, _ = self.minimize(game_copy, depth - 1, alpha, beta)
            if score > max_score:
                max_score = score
                best_move = move
            alpha = max(alpha, max_score)
            if alpha >= beta:
                break  # Beta pruning
        return max_score, best_move

    def minimize(self, game, depth, alpha, beta):
        if depth == 0 or game.is_terminal_state():
            return self.heuristic_strategy(game), None

        min_score = float('inf')
        best_move = None

        for move in game.get_valid_moves(3 - self.player_color):
            game_copy = copy.deepcopy(game)
            game_copy.make_move(*move)
            score, _ = self.maximize(game_copy, depth - 1, alpha, beta)
            if score < min_score:
                min_score = score
                best_move = move
            beta = min(beta, min_score)
            if beta <= alpha:
                break  # Alpha pruning
        return min_score, best_move
