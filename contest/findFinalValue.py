from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original = original * 2
        return original


if __name__ == "__main__":
    func = Solution().findFinalValue
    nums = []
    print(func(nums))
