from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] & nums[j] == 0:
                    dp[i] = max(dp[i - 1] + 1, dp[i])
        print(dp)
        return max(dp)


if __name__ == '__main__':
    func = Solution().longestNiceSubarray
    nums = [1, 3, 8, 48, 10]
    print(func(nums))
