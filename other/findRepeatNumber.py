from collections import defaultdict
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        a_dict = defaultdict(int)
        for num in nums:
            if a_dict[num] >= 1:
                return num
            else:
                a_dict[num] += 1