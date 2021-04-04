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
            if val == max_minus and max_minus != 0:
                print(i)
                print(nums2[i] - nums1[i])
            res += val
        print("-------")
        print(res)
        print(max_minus_index)
        if max_minus_index is not None:
            temp = set(nums1)
            nums2_val = nums2[max_minus_index]
            if nums2_val in temp:
                res -= nums2_val
            else:
                nums1_temp = list(temp)
                nums1_temp.sort()
                ind = bisect.bisect(nums1_temp, nums2_val)
                res -= abs(nums2[max_minus_index] - nums1[max_minus_index])
                if ind == 0:
                    res += abs(nums2[max_minus_index] - nums1_temp[1])
                elif ind == len(nums1_temp):
                    res += abs(nums2[max_minus_index] - nums1_temp[-1])
                else:
                    l = min([abs(nums2_val - nums1_temp[ind - 1]),
                             abs(nums2_val - nums1_temp[ind])])
                    res += l
        return res % (10 ** 9 + 7)


if __name__ == '__main__':
    nums1 = [57, 42, 21, 28, 30, 25, 22, 12, 55, 3, 47, 18, 43, 29, 20, 44, 59, 9, 43, 7, 8, 5, 42, 53, 99, 34, 37, 88,
             87, 62,
             38, 68, 31, 3, 11, 61, 93, 34, 63, 27, 20, 48, 38, 5, 71, 100, 88, 54, 52, 15, 98, 59, 74, 26, 81, 38, 11,
             44, 25,
             69, 79, 81, 51, 85, 59, 84, 83, 99, 31, 47, 31, 23, 83, 70, 82, 79, 86, 31, 50, 17, 11, 100, 55, 15, 98,
             11, 90,
             16, 46, 89, 34, 33, 57, 53, 82, 34, 25, 70, 5, 1]
    nums2 = [76, 3, 5, 29, 18, 53, 55, 79, 30, 33, 87, 3, 56, 93, 40, 80, 9, 91, 71, 38, 35, 78, 32, 58, 77, 41, 63, 5,
             21, 67,
             21, 84, 52, 80, 65, 38, 62, 99, 80, 13, 59, 94, 21, 61, 43, 82, 29, 97, 31, 24, 95, 52, 90, 92, 37, 26, 65,
             89, 90,
             32, 27, 3, 42, 47, 93, 25, 14, 5, 39, 85, 89, 7, 74, 38, 12, 46, 40, 25, 51, 2, 19, 8, 21, 62, 58, 29, 32,
             77, 62,
             9, 74, 98, 10, 55, 25, 62, 48, 48, 24, 21]
    # nums1 = [1, 10, 4, 4, 2, 7]
    # nums2 = [9, 3, 5, 1, 7, 4]
    sol = Solution()
    print(sol.minAbsoluteSumDiff(nums1, nums2))
