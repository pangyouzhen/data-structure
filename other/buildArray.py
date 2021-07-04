class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_nums = [None] * len(nums)
        for i, v in enumerate(nums):
            new_nums[i] = nums[nums[i]]
        return new_nums
