from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        nums.sort()
        return [i for i,v in enumerate(nums) if v == target]