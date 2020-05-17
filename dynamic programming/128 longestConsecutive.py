from typing import List

#  这就是改版之后的最长递增子序列
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        dp = [1] * len(nums)
        for x in range(len(nums)):
            for y in range(x):
                if nums[x] - nums[y] == 1:
                    dp[x] = max(dp[x], dp[y] + 1)
        return max(dp) if dp else 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestConsecutive([1, 2, 3, 4, 6, 9]))
