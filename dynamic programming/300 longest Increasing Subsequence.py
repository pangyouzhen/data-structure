# dp[x] = max(dp[x], dp[y] + 1) 其中 y < x 并且 nums[x] > nums[y]

class Solution:
    def lengthOfLIS(self, nums):
        size = len(nums)
        dp = [1] * size
        for x in range(size):
            for y in range(x):
                if nums[x] > nums[y]:
                    dp[x] = max(dp[x], dp[y] + 1)
        return max(dp) if dp else 0


if __name__ == '__main__':
    sol = Solution()
    print("---------------------")
    print(sol.lengthOfLIS([50, 3, 10, 7, 40, 80]))
