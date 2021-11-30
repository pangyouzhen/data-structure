from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) + 1):
            temp = []
            for j in nums:
                if j >= i:
                    temp.append(j)
            if len(temp) == i:
                return i
        return -1