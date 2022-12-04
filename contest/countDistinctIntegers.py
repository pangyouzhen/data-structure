from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        nums_set = set(nums)
        reverse_set = set([int(str(i)[::-1]) for i in nums])
        return len(nums_set | reverse_set)
