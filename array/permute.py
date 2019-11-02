from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i, v in enumerate(nums):
            pass

    def fn(self, nums, memo):
        if len(nums) == 1:
            return nums
        else:
            return


if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1, 2, 3]))
