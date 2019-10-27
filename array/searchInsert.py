from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, v in enumerate(nums):
            if v >= target:
                return i
            elif i == len(nums) - 1:
                return len(nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))
    print(sol.searchInsert([1, 3, 5, 6], 2))
    print(sol.searchInsert([1, 3, 5, 6], 7))
    print(sol.searchInsert([1, 3, 5, 6], 0))
