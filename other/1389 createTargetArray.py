from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i, v in enumerate(index):
            res.insert(v, nums[v])
        return res
