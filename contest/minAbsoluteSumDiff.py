from typing import List
import bisect


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        max_minus = 0
        res = 0
        max_minus_index = None
        for i in range(n):
            val = abs(nums2[i] - nums1[i])
            if val > max_minus:
                max_minus = val
                max_minus_index = i
            res += val
        print("-------")
        print(res)
        print("max_minus_index is", max_minus_index)
        print("val is ", nums1[max_minus_index], nums2[max_minus_index])
        if max_minus_index is not None:
            res = self.method_name(max_minus_index, nums1, nums2, res)
        return res % (10 ** 9 + 7)

    def method_name(self, max_minus_index, nums1, nums2, res):
        temp = set(nums1)
        nums2_val = nums2[max_minus_index]
        if nums2_val in temp:
            res -= abs(nums2[max_minus_index] - nums1[max_minus_index])
        else:
            nums1_temp = list(temp)
            nums1_temp.sort()
            ind = bisect.bisect(nums1_temp, nums2_val)
            res -= abs(nums2[max_minus_index] - nums1[max_minus_index])
            if ind == 0:
                res += abs(nums2[max_minus_index] - nums1_temp[0])
            elif ind == len(nums1_temp):
                res += abs(nums2[max_minus_index] - nums1_temp[-1])
            else:
                l = min([abs(nums2_val - nums1_temp[ind - 1]),
                         abs(nums2_val - nums1_temp[ind])])
                res += l
        return res


if __name__ == '__main__':
    nums1 = [38, 48, 73, 55, 25, 47, 45, 62, 15, 34, 51, 20, 76, 78, 38, 91, 69, 69, 73, 38, 74, 75, 86, 63, 73, 12,
             100, 59,
             29, 28, 94, 43, 100, 2, 53, 31, 73, 82, 70, 94, 2, 38, 50, 67, 8, 40, 88, 87, 62, 90, 86, 33, 86, 26, 84,
             52, 63,
             80, 56, 56, 56, 47, 12, 50, 12, 59, 52, 7, 40, 16, 53, 61, 76, 22, 87, 75, 14, 63, 96, 56, 65, 16, 70, 83,
             51, 44,
             13, 14, 80, 28, 82, 2, 5, 57, 77, 64, 58, 85, 33, 24]
    nums2 = [90, 62, 8, 56, 33, 22, 9, 58, 29, 88, 10, 66, 48, 79, 44, 50, 71, 2, 3, 100, 88, 16, 24, 28, 50, 41, 65,
             59, 83,
             79, 80, 91, 1, 62, 13, 37, 86, 53, 43, 49, 17, 82, 27, 17, 10, 89, 40, 82, 41, 2, 48, 98, 16, 43, 62, 33,
             72, 35,
             10, 24, 80, 29, 49, 5, 14, 38, 30, 48, 93, 86, 62, 23, 17, 39, 40, 96, 10, 75, 6, 38, 1, 5, 54, 91, 29, 36,
             62, 73,
             51, 92, 89, 88, 74, 91, 87, 34, 49, 56, 33, 67]
    # nums1 = [1, 10, 4, 4, 2, 7]
    # nums2 = [9, 3, 5, 1, 7, 4]
    sol = Solution()

    # print(sol.get_nums_max_index(nums1, nums2))
    print(sol.minAbsoluteSumDiff(nums1, nums2))
