from typing import List


class Solution(object):
    # 最长递增子序列
    def canBeIncreasing(self, nums: List[int]):
        l = len(nums)
        dp = [1] * l
        for i in range(l):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        if max(dp) == len(nums) - 1 or max(dp) == len(nums):
            return True
        return False


if __name__ == '__main__':
    # a = [10, 1, 2, 5, 7]
    a = [105, 924, 32, 968]
    sol = Solution()
    print(sol.canBeIncreasing(a))
