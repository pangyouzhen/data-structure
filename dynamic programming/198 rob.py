from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if 0 < n <= 2:
            return max(nums)
        elif n == 0:
            return 0
        dp = [0] * n
        dp[0], dp[1] = nums[0], nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i - 1], max(dp[:i - 1]) + nums[i])
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([2, 7, 9, 3, 1]) == 12
