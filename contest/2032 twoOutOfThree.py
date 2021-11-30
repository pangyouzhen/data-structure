from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        a1 = set(nums1).intersection(nums2)
        a2 = set(nums1).intersection(nums3)
        a3 = set(nums2).intersection(nums3)
        a = set(a1).union(a2).union(a3)
        return list(a)


if __name__ == '__main__':
    nums1 = [1, 1, 3, 2]
    nums2 = [2, 3]
    nums3 = [3]
    func = Solution().twoOutOfThree(nums1, nums2, nums3)
    print(func)
