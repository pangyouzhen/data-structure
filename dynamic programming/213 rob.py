from typing import List


class Solution:
    # todo
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        dp = [0] * len(nums)
        dp[0] = max(dp[0], dp[1])
        dp[1] = max(dp[0], dp[1])
        for i in nums:
            pass
        pass


if __name__ == '__main__':
    nums = [2, 3, 2]
    sol = Solution()
    print(sol.rob(nums))
