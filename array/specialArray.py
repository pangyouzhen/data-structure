from bisect import bisect_left
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n + 1):
            ind = bisect_left(nums, i)
            if i == (len(nums) - ind):
                return i
        return -1


if __name__ == '__main__':
    nums = [0, 4, 3, 0, 4]
    func = Solution().specialArray
    print(func(nums))
