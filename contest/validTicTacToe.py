from typing import List
from collections import Counter


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        all_boards = "".join(board)
        if len(all_boards) != 9:
            return False
        c = Counter(all_boards)
        if "X" in c.keys() and "O" in c.keys():
            x_val = c["X"]
            o_val = c["X"]
            if x_val < o_val:
                return False
            if x_val - o_val > 1:
                return False
            if x_val <= 3 and o_val <= 2:
                return True
        elif "X" in c.keys() and "O" not in c.keys():
            return c["X"] == 1
        elif "X" not in c.keys() and "O" in c.keys():
            return False
        else:
            return True

    def is_aplha(self, board: List[str], alpha_type: str) -> bool:
        ind = board[0].index(alpha_type)
        pass
