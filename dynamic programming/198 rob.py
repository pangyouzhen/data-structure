from typing import List


class Solution:
    # todo
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        pass


if __name__ == '__main__':
    sol = Solution()
    assert sol.rob([1, 2, 3, 1]) == 4
    assert sol.rob([2, 7, 9, 3, 1]) == 12
