from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i, v in enumerate(nums):
            if i != v:
                return i
        return len(nums)


if __name__ == '__main__':
    a = [3, 0, 1]
    sol = Solution()
    print(sol.missingNumber(a))
