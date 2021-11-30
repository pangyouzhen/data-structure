from typing import List
from collections import defaultdict


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        global res
        res = [0]
        nums1.sort()
        nums2.sort()
        self.count_(nums1, nums2)
        # print(res[0])
        self.count_(nums2, nums1)
        return res[0]

    def count_(self, nums1, nums2):
        global res
        nums1_square = [i ** 2 for i in nums1]
        m = defaultdict(int)
        for i, v_val in enumerate(nums2):
            for j, j_val in enumerate(nums2[i + 1:]):
                val = v_val * j_val
                if val in m:
                    m[val] += 1
                else:
                    m[val] = 1
        # print(m)
        for i in nums1_square:
            if i in m.keys():
                res[-1] += m[i]


if __name__ == '__main__':
    # nums1 = [4, 7, 9, 11, 23]
    # nums2 = [3, 5, 1024, 12, 18]
    nums1 = [1, 1]
    nums2 = [1, 1, 1]
    sol = Solution()
    print(sol.numTriplets(nums1, nums2))
