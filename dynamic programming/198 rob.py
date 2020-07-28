from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 这种 写法算是dp了毕竟是从下面往上推导，没有使用递归的公式
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        memo = [-1] * n
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
        for i in range(2, n):
            res = max(memo[i - 2] + nums[i], memo[i - 1])
            memo[i] = res
        return memo[n - 1]


if __name__ == '__main__':
    sol = Solution()
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([2, 7, 9, 3, 1]) == 12
