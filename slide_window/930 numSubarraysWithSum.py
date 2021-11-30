from typing import List


class Solution:
    #  暴力解法
    def numSubarraysWithSum_(self, nums: List[int], goal: int) -> int:
        res = 0
        l = len(nums)
        for i in range(l):
            for j in range(i + 1, l + 1):
                n = nums[i:j]
                if sum(n) == goal:
                    res += 1
        return res

    # 不定长的滑动窗口
    # 不定长的滑动窗口本身就是快慢指针问题，快指针不断往前移动，慢指针等到条件时候进行移动
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if not nums:
            return 0
        val = [nums[0]]
        quick = 1
        slow = 0
        for i in range(quick, len(nums)):
            val = nums[slow:quick]


if __name__ == '__main__':
    func = Solution().numSubarraysWithSum_
    # nums = [0, 0, 0, 0, 0]
    # goal = 0
    nums = [1, 0, 1, 0, 1]
    goal = 2
    print(func(nums, goal))
