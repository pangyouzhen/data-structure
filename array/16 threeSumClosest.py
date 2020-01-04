# two pointers
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        result = nums[0] + nums[1] + nums[-1]

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if abs(target - val) < abs(result - target):
                    # closest
                    result = val
                if val == target:
                    return target
                elif val > target:
                    r = r - 1
                else:
                    l = l + 1
        return result


if __name__ == '__main__':
    nums = [-1, 2, 1, -4]
    sol = Solution()
    print(sol.threeSumClosest(nums, target=1))
