from typing import List
from bisect import bisect


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return bisect(nums, target)
