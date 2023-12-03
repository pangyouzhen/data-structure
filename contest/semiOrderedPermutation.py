from typing import List


class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        min_index = nums.index(1)
        max_index = nums.index(len(nums))
        total = 0
        total += min_index
        total += len(nums) - 1 - max_index
        if max_index < min_index:
            total -= 1
        return total