from typing import List
import pysnooper


class Solution:
    # @pysnooper.snoop()
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        all_num = [i / x for j in grid for i in j]
        if len(all_num) == 1:
            return 0
        all_num_bool = []
        for i in all_num:
            if i == int(i):
                all_num_bool.append(True)
            else:
                all_num_bool.append(False)
            if len(set(all_num_bool)) == 2:
                return -1
        all_num.sort()
        mid = int(len(all_num) / 2)
        c = len(all_num) % 2
        res = 0
        if c == 0:
            res = sum(all_num[mid:]) - sum(all_num[:mid])
        if c == 1:
            res = sum(all_num[mid+1:]) - sum(all_num[:mid])
        return int(res)


if __name__ == '__main__':
    # grid = [[1, 2, 3], [3, 4, 5], [7, 8, 9]]
    # x = 1
    # grid =[[529, 529, 989], [989, 529, 345], [989, 805, 69]]
    # x = 92
    # grid = [[931, 128], [639, 712]]
    # x = 73
    grid =[[980, 476, 644, 56], [644, 140, 812, 308], [812, 812, 896, 560], [728, 476, 56, 812]]
    x = 84
    func = Solution().minOperations(grid, x)
    print(func)
