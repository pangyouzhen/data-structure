from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = len(nums)
        for i in range(l - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        zeros = nums.count(0)
        res = [i for i in nums if i != 0]
        res.extend(zeros * [0])
        return res
