from typing import List


# TODO
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n
        ans = float("-inf")

        for i in range(1, n+1):
            max_dp[i] = max(max_dp[i-1] * nums[i-1],
                            min_dp[i-1] * nums[i-1], nums[i-1])
            min_dp[i] = min(max_dp[i-1] * nums[i-1],
                            min_dp[i-1] * nums[i-1], nums[i-1])
            ans = max(ans, max_dp[i])
        print(max_dp)
        print(min_dp)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProduct([-2, 0, -1]))
    print(sol.maxProduct([2, 3, -2, 4]))
    print(sol.maxProduct([2, -3, 4, -5]))
