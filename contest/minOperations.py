from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []

        for j in queries:
            v = []
            for i in nums:
                v.append(abs(j - i))
            res.append(sum(v))
        return res
