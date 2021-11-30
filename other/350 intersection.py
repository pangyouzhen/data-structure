from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = Counter(nums1)
        b = Counter(nums2)
        res = []
        a_key = set(a.keys())
        b_key = set(b.keys())
        common_key = a_key.intersection(b_key)
        for i in common_key:
            res.extend(min(a[i], b[i]) * [i])
        return res
