from typing import List
import heapq
from functools import reduce

# TODO timeout
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k > 0:
            min_val = heapq.heappop(nums)
            heapq.heappush(nums,min_val + 1)
            k -= 1
        l = list(nums)
        return reduce(lambda x,y:x*y,nums) % (10 ** 9 +7)

if __name__ == "__main__":
    func = Solution().maximumProduct
    # nums = [0,4]
    # k = 5
    # nums = [6,3,3,2]
    # k = 2
    nums = [24,5,64,53,26,38]
    k = 54
    print(func(nums,k))