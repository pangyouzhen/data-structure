from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if len(nums) < 2:
            return False
        if s % 2 != 0:
            return False
        target = int(s / 2)
        n = len(nums)
        dp = [[False] * (target + 1) for i in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(1, target + 1):
                if j > nums[i]:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n - 1][target]


if __name__ == '__main__':
    sol = Solution()
    func = sol.canPartition
    assert func([1, 5, 11, 5]) is True
    assert func([1, 3, 4, 4]) is False
    assert func([2, 2, 1, 1]) is True
    assert func([1, 2, 5]) is False
