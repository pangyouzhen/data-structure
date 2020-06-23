from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        left = 0
        n = len(nums)
        nums.sort()
        right = n - 1
        left_value = nums[0]
        right_value = nums[-1]
        while left <= right:
            if left_value == right_value:
                right -= 1
                left += 1
            elif left_value > right_value:
                right -= 1
                right_value += nums[right]
            else:
                left += 1
                left_value += nums[left]
        return False


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    sol = Solution()
    print(sol.canPartition(nums))
    nums2 = [1, 2, 3, 5]
    print(sol.canPartition(nums2))
