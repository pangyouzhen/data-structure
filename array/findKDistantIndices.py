from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        inds = []
        for i,v in enumerate(nums):
            if v == key:
                inds.append(i)
        res = []
        for i,v in enumerate(nums):
            for ind in inds:
                if abs(i-ind) <= k:
                    res.append(i)
                    break
        return res
        