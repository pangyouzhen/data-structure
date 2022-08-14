from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        l = len(grid)
        for i in range(l-2):
            one_ans = []
            for j in range(l-2):
                m = max(self.matrix_by_index(grid,i,j))
                one_ans.append(m)
            res.append(one_ans)
        return res

    def matrix_by_index(self,grid: List[List[int]], row_index: int, col_index: int):
        a = []
        for i in grid[row_index:row_index+3]:
            a.extend(i[col_index:col_index+3])
        return a

if __name__ == "__main__":
    func = Solution().largestLocal
    # grid = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [
    #     1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
    grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
    print(func(grid))
    # func2 = Solution().matrix_by_index
    # print(func2(grid,1,1))
