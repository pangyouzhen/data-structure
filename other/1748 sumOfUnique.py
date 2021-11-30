from typing import List
from collections import Counter


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        a = 0
        for k, v in nums_counter.items():
            if v == 1:
                a += k
        return a
