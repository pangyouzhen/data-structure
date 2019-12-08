class Solution:

    def lengthOfLIS(self, nums):
        dp = [0] * len(nums)
        dp[0] = 1
        max_value = 1
        for i in range(len(nums)):
            max_value = 0
            for j in range(1, i):
                if nums[i] > nums[j]:
                    max_value = max(max_value, dp[j])
            dp[i] = max_value + 1
            max_value = max(max_value, dp[i])
        return max_value


if __name__ == '__main__':
    sol = Solution()
    # [3,] = [3,]
    # assert sol.lengthOfLIS([3]) == 1
    # [3, 10,] = [3, 10,]
    # assert sol.lengthOfLIS([3, 10, ]) == 2
    # [3, 10, 2,] = [3, 10,]
    assert sol.lengthOfLIS([3, 10, 2, ]) == 2
    # [3, 10, 2, 1] = [3, 10]
    assert sol.lengthOfLIS([3, 10, 2, 1]) == 2
    # [3, 10, 2, 1, 20] = [3, 10, 20]
    assert sol.lengthOfLIS([3, 10, 2, 1, 20]) == 3
    # [4,] = [4,]
    assert sol.lengthOfLIS([4]) == 1
    # [4, 5] = [4, 5,]
    assert sol.lengthOfLIS([4, 5, ]) == 2
    # [4, 5, 1,] = [4, 5]
    assert sol.lengthOfLIS([4, 5, 1, ]) == 2
    # [4, 5, 1, 2] = [4, 5,] /// [1,2]
    assert sol.lengthOfLIS([4, 5, 1, 2]) == 2
    # [4, 5, 1, 2, 3] = [1, 2, 3]
    assert sol.lengthOfLIS([4, 5, 1, 2, 3]) == 3
    # 如果新增的数比上一个的最大值小则判断次小的如果比次小的长度的最小值
    # +1 or +0
    #     [50, 3]  = [3,] / [50]
    assert sol.lengthOfLIS([50, 3, ]) == 1
    #     [50, 3, 10,]  = [3, 10]
    assert sol.lengthOfLIS([50, 3, 10, 7, ]) == 2
    #     [50, 3, 10, 7, 40]  = [3, 7, 40]
    assert sol.lengthOfLIS([50, 3, 10, 7, 40]) == 3
    #     [50, 3, 10, 7, 40, 80]  = [3, 7, 40, 80]
    assert sol.lengthOfLIS([50, 3, 10, 7, 40, 80]) == 4
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
