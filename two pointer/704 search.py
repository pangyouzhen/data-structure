from typing import List
import math


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1

        # if not nums:
        #     return -1
        # mid = math_.floor(len(nums) / 2)
        # if nums[mid] == target:
        #     return True
        # elif nums[mid] > target:
        #     nums = nums[:mid]
        #     return self.search(nums, target)
        # else:
        #     nums = nums[mid + 1:]
        #     return self.search(nums, target)


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 12
    sol = Solution()
    print(sol.search(nums, target))
