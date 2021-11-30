class Solution(object):

    #  这个题如果改成 子序列呢
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
        return max(dp)


if __name__ == '__main__':
    # nums = [10, 30, 60, 60, 60, 65]
    nums = [10, 20, 30, 5, 10, 50]
    sol = Solution()
    print(sol.maxAscendingSum(nums))
