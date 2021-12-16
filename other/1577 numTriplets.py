import collections
from typing import List


class Solution:
    def __init__(self):
        self.res = 0

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        self.count_(nums1, nums2)
        self.count_(nums2, nums1)
        return self.res

    def count_(self, nums1: List[int], nums2: List[int]) -> None:
        l2 = len(nums2)
        nums1_square = [i ** 2 for i in nums1]
        m = collections.defaultdict(int)
        for j in range(l2):
            for i in range(j + 1, l2):
                val = nums2[i] * nums2[j]
                m[val] += 1
        for i in nums1_square:
            if i in m.keys():
                self.res += m[i]


if __name__ == '__main__':
    # nums1 = [4, 7, 9, 11, 23]
    # nums2 = [3, 5, 1024, 12, 18]
    nums1 = [1, 1]
    nums2 = [1, 1, 1]
    sol = Solution()
    print(sol.numTriplets(nums1, nums2))
