from typing import List


class Solution:
    def __init__(self) -> None:
        self.res = 0
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        def delete_value(grid:List[List[int]]):
            if not grid[0]:
                return 
            tmp = []
            for i in grid:
                max_val = max(i)
                tmp.append(max_val)
                ind = i.index(max_val)
                del i[ind]
            m = max(tmp) 
            self.res += m
            delete_value(grid)
        delete_value(grid)
        return self.res

if __name__ == "__main__":
    func = Solution().deleteGreatestValue
    grid = [[1,2,4],[3,3,1]]
    print(func(grid))