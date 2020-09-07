# dp[x] = max(dp[x], dp[y] + 1) 其中 y < x 并且 nums[x] > nums[y]

# 这是dp从底往上求解的，如果从顶层到底层呢
#  这里思维的一个误区是： 和前一个数进行比较，dp公式中并没有指明 x = y + 1，而是对每一个进行比较
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
    # print(sol.lengthOfLIS([50, 3, 10, 7, 40, 80]))
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [10, 2, 9, 3, 11, 5]
    for i in range(1, len(nums)):
        print(nums[:i])
        print(sol.lengthOfLIS(nums[:i]))
        print("-------------------------")
