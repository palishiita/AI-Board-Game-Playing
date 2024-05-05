import copy
from MiniMax import MiniMaxPlayer

class AlphaBetaPlayer(MiniMaxPlayer):
    def __init__(self, player_color, max_depth, heuristic_strategy, strategies):
        """
        Initialize the AlphaBetaPlayer.

        Args:
            player_color (int): The color of the player.
            max_depth (int): The maximum depth to search in the game tree.
            heuristic_strategy (function): The heuristic evaluation function.
            strategies (list): List of heuristic strategies to consider.
        """
        super().__init__(player_color, max_depth, heuristic_strategy)
        self.strategies = strategies

    def get_best_move(self, game):
        """
        Get the best move for the current player using Alpha-Beta pruning.

        Args:
            game (Reversi): The game state.

        Returns:
            tuple: The best move coordinates.
        """
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
        """
        Calculate the maximum value for the current player.

        Args:
            game (Reversi): The game state.
            alpha (float): The alpha value for Alpha-Beta pruning.
            beta (float): The beta value for Alpha-Beta pruning.
            depth (int): The current depth in the game tree.

        Returns:
            float: The maximum value.
        """
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
        """
        Calculate the minimum value for the opponent player.

        Args:
            game (Reversi): The game state.
            alpha (float): The alpha value for Alpha-Beta pruning.
            beta (float): The beta value for Alpha-Beta pruning.
            depth (int): The current depth in the game tree.

        Returns:
            float: The minimum value.
        """
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
        """
        Evaluate the current game state using the specified heuristic strategy.

        Args:
            game (Reversi): The game state.

        Returns:
            float: The evaluation score.
        """
        # Evaluate the current game state using the specified heuristic strategy
        return self.strategies[0](game)
