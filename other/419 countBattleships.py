from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        pass
if __name__ == '__main__':
    func = Solution().countBattleships
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    print(func(board))