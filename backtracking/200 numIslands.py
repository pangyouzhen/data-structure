from typing import List


# 回溯法+方向判断

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        global m
        m = len(grid)
        global n
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(grid,i,j)
        return res
    
    def dfs(self,grid:List[List[str]],col:int,row:int):
        # 这里不能用try判断是否超出边界，因为python支持负索引的
        # 主要就是遍历过的进行染色
        if  0 <= col< m and 0<= row < n:
            if grid[col][row] == "1":
                grid[col][row] = '2'
                # print(grid)
                for l,r in [[-1,0],[1,0],[0,1],[0,-1]]:
                    self.dfs(grid,col+l,row+r)
                    
if __name__ == '__main__':
    # nums = [
    #     ['1', '1', '0', '0', '0'],
    #     ['1', '1', '0', '0', '0'],
    #     ['0', '0', '1', '0', '0'],
    #     ['0', '0', '0', '1', '1']
    # ]
    nums = [["1","0","1","1","0","1","1"]]
    sol = Solution()
    print(sol.numIslands(grid=nums))
