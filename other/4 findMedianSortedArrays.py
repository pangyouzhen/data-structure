from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        even = len(nums1) % 2
        mid = len(nums1) // 2
        if even != 0:
            return nums1[mid]
        else:
            return (nums1[mid - 1] + nums1[mid]) / 2


if __name__ == '__main__':
    sol = Solution()
    sol.findMedianSortedArrays()