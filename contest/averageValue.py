from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if i % 3 == 0 and i % 2 == 0:
                res.append(i)
        if res:
            return int(sum(res) / len(res))
        return 0
