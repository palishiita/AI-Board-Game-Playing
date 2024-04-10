class HeuristicEvaluator:

    def __init__(self, player_color):
        self.player_color = player_color

    def heuristic_strategy_1(self, game):
        """
        Heuristic Strategy 1: Coin Parity
        """
        max_score = sum(row.count(self.player_color) for row in game.board)
        min_score = sum(row.count(3 - self.player_color) for row in game.board)
        return max_score - min_score

    def heuristic_strategy_2(self, game):
        """
        Heuristic Strategy 2: Mobility
        """
        max_mobility = len(game.get_valid_moves(self.player_color))
        min_mobility = len(game.get_valid_moves(3 - self.player_color))
        return max_mobility - min_mobility

    def heuristic_strategy_3(self, game):
        """
        Heuristic Strategy 3: Mobility and Corners
        """
        max_mobility = len(game.get_valid_moves(self.player_color))
        min_mobility = len(game.get_valid_moves(3 - self.player_color))

        max_corners = sum(game.board[i][j] == self.player_color for i, j in [(0, 0), (0, 7), (7, 0), (7, 7)])
        min_corners = sum(game.board[i][j] == 3 - self.player_color for i, j in [(0, 0), (0, 7), (7, 0), (7, 7)])

        return (max_mobility + max_corners) - (min_mobility + min_corners)

    def heuristic_strategy_4(self, game):
        """
        Heuristic Strategy 4: Mobility and Stability
        """
        max_mobility = len(game.get_valid_moves(self.player_color))
        min_mobility = len(game.get_valid_moves(3 - self.player_color))

        max_stability = self.calculate_stability(game, self.player_color)
        min_stability = self.calculate_stability(game, 3 - self.player_color)

        return (max_mobility + max_stability) - (min_mobility + min_stability)

    def heuristic_strategy_5(self, game):
        """
        Heuristic Strategy 5: Mobility, Corners, and Edges
        """
        max_mobility = len(game.get_valid_moves(self.player_color))
        min_mobility = len(game.get_valid_moves(3 - self.player_color))

        max_corners = sum(game.board[i][j] == self.player_color for i, j in [(0, 0), (0, 7), (7, 0), (7, 7)])
        min_corners = sum(game.board[i][j] == 3 - self.player_color for i, j in [(0, 0), (0, 7), (7, 0), (7, 7)])

        max_edges = self.calculate_edges(game, self.player_color)
        min_edges = self.calculate_edges(game, 3 - self.player_color)

        return (max_mobility + max_corners + max_edges) - (min_mobility + min_corners + min_edges)

    def heuristic_strategy_6(self, game):
        """
        Heuristic Strategy 6: Mobility, Corners, Edges, and Stability
        """
        max_mobility = len(game.get_valid_moves(self.player_color))
        min_mobility = len(game.get_valid_moves(3 - self.player_color))

        max_corners = sum(game.board[i][j] == self.player_color 
                          for i, j in [(0, 0), (0, 7), (7, 0), (7, 7)])
        min_corners = sum(game.board[i][j] == 3 - self.player_color 
                          for i, j in [(0, 0), (0, 7), (7, 0), (7, 7)])

        max_edges = self.calculate_edges(game, self.player_color)
        min_edges = self.calculate_edges(game, 3 - self.player_color)

        max_stability = self.calculate_stability(game, self.player_color)
        min_stability = self.calculate_stability(game, 3 - self.player_color)

        return (max_mobility + max_corners + max_edges + max_stability) - (min_mobility + min_corners + min_edges + min_stability)

    def calculate_edges(self, game, player_color):
        """
        Calculate the number of disks along the edges for the specified player color
        """
        edges = [(0, j) for j in range(8)] + [(i, 0) for i in range(8)] + [(7, j) for j in range(8)] + [(i, 7) for i in range(8)]
        return sum(game.board[i][j] == player_color for i, j in edges)

    def calculate_stability(self, game, player_color):
        """
        Calculate the stability of disks for the specified player color
        """
        stable_count = 0

        # Iterate through each cell on the board
        for i in range(8):
            for j in range(8):
                if game.board[i][j] != player_color:
                    continue  # Skip if not player's disk

                # Check if the disk is stable
                if self.is_stable(game, i, j, player_color):
                    stable_count += 1

        return stable_count

    def is_stable(self, game, row, col, player_color):
        """
        Check if the disk at the given position is stable for the specified player color
        """
        # Check if the disk is in one of the four corners
        if (row, col) in [(0, 0), (0, 7), (7, 0), (7, 7)]:
            return True

        # Check if the disk is in a row or column of the same color that ends at a corner
        for dr, dc in [(0, 1), (1, 0)]:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8 and game.board[r][c] == player_color:
                r += dr
                c += dc
            if (r, c) in [(0, 0), (0, 7), (7, 0), (7, 7)]:
                return True

        return False