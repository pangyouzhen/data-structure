from typing import List
from bisect import insort


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        while k > 0:
            a = nums[0]
            nums = nums[1:]
            insort(nums, -a)
            k -= 1
        return sum(nums)


if __name__ == '__main__':
    nums = [2, -3, -1, 5, -4]
    k = 2
    func = Solution().largestSumAfterKNegations
    print(func(nums, k))
