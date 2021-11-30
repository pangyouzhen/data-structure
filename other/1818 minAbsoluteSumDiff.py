from typing import List
from bisect import bisect_right
import pysnooper


class Solution:
    @pysnooper.snoop()
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        minus_val = 0
        minus_ind = float("inf")
        for ind, (i, v) in enumerate(zip(nums1, nums2)):
            val = abs(i - v)
            if val > minus_val:
                minus_val = val
                minus_ind = ind
            res += val
        if res == 0:
            return res
        else:
            nums1_val = nums1[minus_ind]
            nums2_val = nums2[minus_ind]
            res -= abs(nums1_val - nums2_val)
            sort_num1 = sorted(nums1)
            insert_ind = bisect_right(sort_num1, nums2_val)
            if insert_ind == len(sort_num1):
                res += abs(nums2_val - sort_num1[insert_ind - 1])
            else:
                res += min(abs(nums2_val - sort_num1[insert_ind - 1]), abs(nums2_val - sort_num1[insert_ind]))
        return res


if __name__ == '__main__':
    # nums1 = [1, 7, 5]
    # nums2 = [2, 3, 5]
    # nums1 = [1, 10, 4, 4, 2, 7]
    # nums2 = [9, 3, 5, 1, 7, 4]
    nums1 = [45, 86, 75, 27, 10, 44, 27, 13, 100, 17, 7, 50, 54, 90, 17, 59, 54, 26, 85, 89, 81, 6, 65, 43, 14, 4, 24,
             58, 51,
             49, 40, 24, 56, 59, 32, 93, 17, 63, 62, 24, 76, 27, 86, 11, 77, 33, 45, 87, 64, 27, 47, 13, 15, 93, 78, 44,
             94, 26,
             40, 69, 13, 100, 65, 38, 85, 95, 98, 59, 67, 90, 12, 24, 67, 86, 11, 56, 94, 16, 35, 27, 13, 39, 31, 69,
             52, 32,
             72, 82, 56, 73, 94, 28, 45, 35, 68, 76, 100, 52, 27, 85]
    nums2 = [37, 53, 98, 10, 39, 26, 19, 66, 84, 6, 31, 78, 29, 84, 7, 63, 14, 87, 11, 13, 61, 42, 6, 3, 35, 67, 62, 49,
             38, 7, 74, 12, 65, 37, 2, 58, 50, 55, 86, 7, 75, 88, 35, 56, 90, 77, 5, 28, 5, 59, 79, 70, 31, 22, 70, 37,
             69, 49, 62, 85, 9, 87, 100, 7, 79, 92, 91, 20, 95, 51, 83, 58, 8, 82, 100, 18, 48, 60, 7, 80, 89, 66, 64,
             11, 22, 69, 59, 70, 76, 10, 48, 12, 86, 31, 15, 16, 38, 59, 41, 82]
    sol = Solution()
    print(sol.minAbsoluteSumDiff(nums1, nums2))
