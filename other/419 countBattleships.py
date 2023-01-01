from typing import List

# 419
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        pass
if __name__ == '__main__':
    func = Solution().countBattleships
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    print(func(board))