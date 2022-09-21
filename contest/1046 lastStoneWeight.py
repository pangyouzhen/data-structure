from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        while len(stones) > 1:
            heapq.heapify(stones)
            fst = heapq.heappop(stones)
            sed = heapq.heappop(stones)
            if fst != sed:
                minus = fst - sed
                heapq.heappush(stones, minus)
        if len(stones) == 1:
            return -list(stones)[0]
        return 0


if __name__ == "__main__":
    func = Solution().lastStoneWeight
    nums = [2, 7, 4, 1, 8, 1]
    print(func(nums))
