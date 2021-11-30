from typing import List
from bisect import bisect


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort_nums = sorted(nums)
        return [sort_nums.index(i) for i in nums]
