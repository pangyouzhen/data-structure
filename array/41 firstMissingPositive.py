from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0 or nums[0] > 1 or nums[-1] < 1:
            return 1

        for i in range(1, nums[-1]):
            if i not in nums:
                return i
        return nums[-1] + 1


if __name__ == '__main__':
    sol = Solution()
    # assert  sol.firstMissingPositive([1, 2, 0]) == 3
    print(sol.firstMissingPositive([1, 2, 0]))
    print(sol.firstMissingPositive([3, 4, -1, 1]))
    print(sol.firstMissingPositive([]))
    print(sol.firstMissingPositive([1, 1000]))
