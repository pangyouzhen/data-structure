from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1:
            return [nums]
        result = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i + 1:]
            for y in self.permuteUnique(n):
                ans = [num] + y
                if ans not in result:
                    result.append([num] + y)
        return result

