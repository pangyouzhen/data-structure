from typing import List


class Solution:
    # TODO
    def matrixScore(self, grid: List[List[int]]) -> int:
        grid = [str(i) for i in grid for j in i]
        for g in grid:
            res = int("".join(g),2)
        

if __name__ == '__main__':
    nums = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]

