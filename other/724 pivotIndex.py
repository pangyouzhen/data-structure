from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1


if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    sol = Solution()
    print(sol.pivotIndex(nums))
