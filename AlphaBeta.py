import copy
from MiniMax import MiniMaxPlayer

class AlphaBetaPlayer(MiniMaxPlayer):
    def __init__(self, player_color, max_depth, heuristic_strategy, strategies):
        super().__init__(player_color, max_depth, heuristic_strategy)
        self.strategies = strategies

    def get_best_move(self, game):
        best_move = None
        alpha = float('-inf')
        beta = float('inf')
        for move in game.get_valid_moves(self.player_color):
            # Apply the move to a deepcopy of the game state
            new_game = copy.deepcopy(game)
            new_game.make_move(*move)

            # Evaluate the move using Alpha-Beta pruning
            value = self.min_value(new_game, alpha, beta, self.max_depth - 1)
            
            if value > alpha:
                alpha = value
                best_move = move

        return best_move

    def max_value(self, game, alpha, beta, depth):
        if depth == 0 or game.is_terminal_state():
            return self.evaluate(game)

        value = float('-inf')
        for move in game.get_valid_moves(self.player_color):
            new_game = copy.deepcopy(game)
            new_game.make_move(*move)
            value = max(value, self.min_value(new_game, alpha, beta, depth - 1))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value

    def min_value(self, game, alpha, beta, depth):
        if depth == 0 or game.is_terminal_state():
            return self.evaluate(game)

        value = float('inf')
        for move in game.get_valid_moves(3 - self.player_color):
            new_game = copy.deepcopy(game)
            new_game.make_move(*move)
            value = min(value, self.max_value(new_game, alpha, beta, depth - 1))
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value

    def evaluate(self, game):
        # Evaluate the current game state using the specified heuristic strategy
        return self.strategies[0](game)