import bisect
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        l = len(nums)
        res = 0
        print(nums)
        for i in range(l):
            ind_left = bisect.bisect_left(nums, lower - nums[i], 0, i)
            ind_right = bisect.bisect_right(nums, upper - nums[i], 0, i)
            print(f"{res=},{ind_right=},{ind_left=},{i=},{l=}")
            res += ind_right - ind_left
        return res


if __name__ == "__main__":
    func = Solution().countFairPairs
    nums = [0, 1, 7, 4, 4, 5]
    lower = 3
    upper = 6
    # nums = [0, 0, 0, 0, 0, 0]
    lower = 0
    upper = 0
    # nums = [7, -2, 2, 8, -1000000000, -1000000000, -1000000000, -1000000000]
    lower = -15
    upper = 11
    print("---------------------------")
    print(func(nums, lower, upper))
    nums.sort()
    print(nums)
    print(bisect.insort_right(nums,8))
    print(nums)
    print(bisect.insort_right(nums,8,0,2))
    print(nums)
    print(bisect.bisect_right(nums,7))
    print(bisect.bisect_right(nums,7,0,2))