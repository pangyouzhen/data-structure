class Solution:
    def maxSubArray(self, nums):
        if len(list(filter(lambda x: x > 0, nums))) == 0:
            return max(nums)
        nums_ls = [None] * (len(nums) + 1)
        return self.maxSubArray_memo(nums, nums_ls)

    def maxSubArray_memo(self, nums, memo):
        memo[0] = 0
        for i, v in enumerate(nums):
            memo_value = memo[i] + nums[i]
            if memo_value > 0:
                memo[i + 1] = memo_value
            else:
                memo[i + 1] = 0
        return max(memo)


# 有一个关键是如果加上这个值后为负数则重新赋值为0
# [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 这个应该从底往上思考，增加一个数字后咋样

if __name__ == '__main__':
    sol = Solution()
    res = sol.maxSubArray
    assert res([-1]) == -1
    assert res([-1, -2]) == -1
    assert res([-2, 1, 1, -2]) == 2
    assert res([-2, 1]) == 1
    assert res([-2, 1, -3]) == 1
    assert res([-2, 1, -3, 4, ]) == 4
    assert res([-2, 1, -3, 4, -1]) == 4
    assert res([-2, 1, -3, 4, -1, 2]) == 5
    assert res([-2, 1, -3, 4, -1, 2, 1]) == 6
    assert res([-2, 1, -3, 4, -1, 2, 1, -5]) == 6
    assert res([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
