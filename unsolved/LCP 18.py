from typing import List
from bisect import bisect_right
from pysnooper import snoop


class Solution:
    def breakfastNumber_(self, staple: List[int], drinks: List[int], x: int) -> int:
        # 暴力解法
        res = 0
        for i in staple:
            for j in drinks:
                if i + j <= x:
                    res += 1
        return res

    @snoop()
    # 使用bisect库维护有序列表
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort(reverse=True)
        drinks.sort()
        res = 0
        for i in staple:
            if i > x:
                continue
            minus = x - i
            ind = bisect_right(drinks, minus)
            res += ind
        return res % 1000000007


if __name__ == '__main__':
    staple = [10, 20, 5]
    drinks = [5, 5, 2]
    x = 15
    # staple = [6, 1, 9, 2, 9, 9, 3, 4]
    # drinks = [2, 7, 10, 2, 9, 2, 1, 3]
    # x = 2
    # staple = [2, 1, 1]
    # drinks = [8, 9, 5, 1]
    # x = 9
    sol = Solution()
    print(sol.breakfastNumber(staple, drinks, x))
