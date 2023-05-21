from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 最大值
        sort_nums = sorted(nums,reverse=True)
        if sort_nums == nums:
            nums = sort_nums[::-1]
        # 一般情况
        # 找到从右到左找到第一个降序的序列
        l = len(sort_nums)
        reverse_num = nums[::-1]
        for i in range(l-1):
            if nums[i] > nums[i-1]:
                pass