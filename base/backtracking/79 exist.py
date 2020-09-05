from typing import List


class Solution:
    def __init__(self):
        self.directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    def exist(self, board: List[List[str]], word: str) -> bool:
        global m, n, visited
        m = len(board)
        n = len(board[0])
        #  这里的m和n 不要搞错，一个外层，一个内层
        visited = [[False] * n for _ in range(m)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.searchWord(board, word, 0, i, j):
                    return True
        return False

    def searchWord(self, board: List[List[str]], word: str, index: int, startx: int, starty: int):
        if index == len(word) - 1:
            return board[startx][starty] == word[index]
        if board[startx][starty] == word[index]:
            visited[startx][starty] = True
            for i in range(4):
                newx = startx + self.directions[i][0]
                newy = starty + self.directions[i][1]
                if self.inArea(newx, newy) and not visited[newx][newy]:
                    if self.searchWord(board, word, index + 1, newx, newy):
                        return True
            visited[startx][starty] = False
        return False

    def inArea(self, x, y):
        return x >= 0 and x < m and y >= 0 and y < n


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    sol = Solution()
    print(sol.exist(board, word))
    board2 = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word2 = "AAB"
    print(sol.exist(board2, word2))
