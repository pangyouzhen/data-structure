from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = list(range(len(nums)))
        for i, v in zip(a, nums):
            if i != v:
                return i
        return len(nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.missingNumber([0]))
