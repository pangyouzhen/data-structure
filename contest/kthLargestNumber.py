from typing import List
import heapq
import pysnooper


class Solution:
    # @pysnooper.snoop()
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(i) for i in nums]
        diff_k = len(nums) - k
        # heapq.heapify(nums)
        # last_val = 0
        # for i in range(diff_k):
        #     last_val = heapq.heappop(nums)
        # return str(last_val)
        nums.sort()
        return str(nums[diff_k])

