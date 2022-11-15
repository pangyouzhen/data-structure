from typing import List


# 回溯法+方向判断
class Solution:
    def __init__(self) -> None:
        self.res = 0
    def numIslands(self, grid: List[List[str]]) -> int:
        global m
        m = len(grid)
        global n
        n = len(grid[0])
        global flag
        flag = [[0] * n for j in range(m)]
        for i in range(m):
            for j in range(n):
                self.dfs(grid,i,j)
        return self.res

    def dfs(self,grid,i,j):
        if i < 0 or j < 0 or i>= m and j>=n :
            return 
        if flag[i][j]==0 and grid[i][j] == '1':
            flag[i][j] = 1
            self.res += 1
            self.dfs(grid,i-1,j)
            self.dfs(grid,i+1,j)
            self.dfs(grid,i,j-1)
            self.dfs(grid,i,j+1)
        
if __name__ == '__main__':
    nums = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1']
    ]
    sol = Solution()
    print(sol.numIslands(grid=nums))
