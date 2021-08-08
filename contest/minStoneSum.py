from typing import List
import pysnooper
import math
from bisect import insort


class Solution:
    # @pysnooper.snoop()
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        piles.sort()
        for i in range(k):
            a = piles.pop()
            remove_val = math.floor(a / 2)
            reverse_val = a - remove_val
            total -= remove_val
            insort(piles, reverse_val)
        return total


# 怎么优化这个时间
# 基本思想就是：最大的数值进行向下取整（向下取整之后的数值还是可能最大的），然后不断重复这个过程 时间超时
if __name__ == '__main__':
    piles = [5, 4, 9]
    k = 2
    sol = Solution().minStoneSum
    print(sol(piles, k))
