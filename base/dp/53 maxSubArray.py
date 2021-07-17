class Solution:
    # 本题使用动态规划 需要从下往上，核心是若前一个元素大于0 则加到当前元素上
    #  f(x) = max(f(x-1)+a ,a)
    def maxSubArray(self, nums):
        memo_arr = [0] * len(nums)
        memo_arr[0] = nums[0]
        for i, v in enumerate(nums[1:]):
            if memo_arr[i] < 0:
                memo_arr[i + 1] = v
            else:
                memo_arr[i + 1] = memo_arr[i] + v
        return max(memo_arr)


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
