class Solution:
    # 本题使用动态规划 需要从下往上，核心是若前一个元素大于0 则加到当前元素上
    #  f(x) = max(f(x-1)+a ,a)
    #  然后求整个数组（动态规划一般都有一个数组）的最大值即可，
    def maxSubArray(self, nums):
        submemo = [0] * len(nums)
        submemo[0] = nums[0]
        for i, v in enumerate(nums[1:]):
            if submemo[i] < 0:
                submemo[i+1] = v
            else:
                submemo[i+1] = submemo[i] + v
        return max(submemo)

# 有一个关键是如果加上这个值后为负数则重新赋值为0
# 按顺序递推和记忆化搜索是实现动态规划的两种方法
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
