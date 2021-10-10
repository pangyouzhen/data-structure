from typing import List
import pysnooper


class Solution:
    """
    .. math::
    min y = |x1 - k| + |x2 -k| + |x3-k| + |....|
    这种求极值的问题是取找到中位数
    """

    @pysnooper.snoop()
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        all_num = [i for j in grid for i in j]
        _ = [i % x for i in all_num]
        if len(all_num) == 1:
            return 0
        elif len(set(_)) >= 2:
            return -1

        def median(data):
            data.sort()
            l = len(data)
            mid_loc = l // 2
            if l % 2 == 1:
                return data[mid_loc]
            else:
                return (data[mid_loc] + data[mid_loc - 1]) / 2

        mid = median(all_num)
        res = 0
        for i in all_num:
            res += abs(i - mid)
        return int(res / x)


if __name__ == '__main__':
    # grid = [[1, 2, 3], [3, 4, 5], [7, 8, 9]]
    # x = 1
    # grid =[[529, 529, 989], [989, 529, 345], [989, 805, 69]]
    # x = 92
    # grid = [[931, 128], [639, 712]]
    # x = 73
    # grid = [[980, 476, 644, 56], [644, 140, 812, 308], [812, 812, 896, 560], [728, 476, 56, 812]]
    # x = 84
    grid = [[980, 437, 889, 386], [45, 655, 891, 659], [751, 705, 333, 436], [452, 155, 603, 775]]
    x = 741
    func = Solution().minOperations(grid, x)
    print(func)
