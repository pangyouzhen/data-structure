from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        fst_group = nums[:n]
        sed_group = nums[n:]
        for i in range(n):
            res.append(fst_group[i])
            res.append(sed_group[i])
        return res
