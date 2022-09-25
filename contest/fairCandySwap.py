from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        s = (sum(aliceSizes) + sum(bobSizes)) / 2
        a = s - sum(aliceSizes)
        a_set = set(aliceSizes)
        b_set = set(bobSizes)
        for i in a_set:
            if (i + a) in b_set:
                return [i, int(i + a)]
