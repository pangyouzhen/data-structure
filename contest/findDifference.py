from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set(nums1).difference(set(nums2))
        b = set(nums2).difference(set(nums1))
        return [list(a),list(b)]