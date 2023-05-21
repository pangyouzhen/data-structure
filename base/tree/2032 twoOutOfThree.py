from typing import List
from collections import defaultdict

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1,nums2,nums3 = set(nums1),set(nums2),set(nums3)
        all_element = nums1 | nums2 | nums3
        res = []
        d = defaultdict(int)
        for i in all_element:
            if i in nums1:
                d[i] += 1
            if i in nums2:
                d[i] += 1
            if i in nums3:
                d[i] += 1
            if d[i] >= 2:
                res.append(i)
        return res