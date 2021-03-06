# dp[x] = max(dp[x], dp[y] + 1) 其中 y < x 并且 nums[x] > nums[y]

# 这是dp从底往上求解的，如果从顶层到底层呢,
# 这个是没法从顶层到底层的，因为顶层的目标是不确定的，无法进行倒推

# 这里的状态没有定义清楚，dp[i] 并不是代表着 最后一个值的LIS，后面的例子很清楚 dp[4] = 2  不是最大长度
# 这里的dp[i] 代表的是以 x[i] 为最后一个值的最大长度，
# 最后 对于整个序列 取max值才是结果
class Solution:
    def lengthOfLIS(self, nums):
        size = len(nums)
        dp = [1] * size
        for x in range(size):
            for y in range(x):
                if nums[x] > nums[y]:
                    dp[x] = max(dp[x], dp[y] + 1)
        print(dp)
        return max(dp) if dp else 0


if __name__ == '__main__':
    sol = Solution()
    print("---------------------")
    # print(sol.lengthOfLIS([50, 3, 10, 7, 40, 80]))
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [10, 2, 9, 3, 11, 5]
    # for i in range(1, len(nums)):
    #     print(nums[:i])
    #     print(sol.lengthOfLIS(nums[:i]))
    #     print("-------------------------")
    print(sol.lengthOfLIS(nums))
    print("********************")
    nums2 = [5, 6, 7, 1, 2]
    print(sol.lengthOfLIS(nums2))
