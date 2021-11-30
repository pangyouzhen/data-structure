from typing import List
import pysnooper
import math
import heapq


class Solution:
    # 最大堆，最小堆
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles)
        for i in range(n):
            piles[i] = -piles[i]
        heapq.heapify(piles)
        for i in range(k):
            tmp = heapq.heappop(piles)
            heapq.heappush(piles, tmp + (-tmp) // 2)
        return -sum(piles)


if __name__ == '__main__':
    piles = [5, 4, 9]
    k = 2
    sol = Solution().minStoneSum
    print(sol(piles, k))
