from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0]
        s = sum(nums)
        n = len(nums)
        left_sum = [nums[0]]
        for i in range(1,n):
            num = left_sum[-1] + 1
            left_sum.append(num)
        print(left_sum)
        right_sum = [s-i for i in left_sum]
        left_sum.insert(0,0)
        right_sum.append(0)
        res = []
        for i,v in zip(left_sum,right_sum):
            res.append(abs(i-v))
        return res