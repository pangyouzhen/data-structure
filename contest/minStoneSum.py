from typing import List
import pysnooper
import math
from bisect import insort


class Solution:
    # todo 原先的是C++代码，不会翻译
    def minStoneSum(self, piles: List[int], k: int) -> int:
        queue = []
        while not queue:
            queue.pop()
        for i in piles:
            queue.append(i)
        for i in range(k):
            v = queue[0]
            queue.pop()
            queue.append(v - v / 2)
        ans = 0
        while not queue:
            ans += queue[0]
            queue.pop()
        return ans


# 怎么优化这个时间
# 基本思想就是：最大的数值进行向下取整（向下取整之后的数值还是可能最大的），然后不断重复这个过程 时间超时
if __name__ == '__main__':
    piles = [5, 4, 9]
    k = 2
    sol = Solution().minStoneSum
    print(sol(piles, k))
