from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums.append(float('-inf'))
        for i in range(len(nums) + 1):
            if nums[i + 1] - nums[i] < 0:
                return i


if __name__ == '__main__':
    sol = Solution()
    nums = [1]
    nums2 = [1, 2, 3, 1]
    nums3 = [1, 2]
    assert sol.findPeakElement(nums) == 0
    assert sol.findPeakElement(nums2) == 2
    assert sol.findPeakElement(nums3) == 1
    print(sol.findPeakElement(nums3))
