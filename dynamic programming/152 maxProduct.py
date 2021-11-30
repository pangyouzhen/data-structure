from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return max(self.maxProduct(nums[:-2]) * nums[-1], self.maxProduct(nums[:-2]))


if __name__ == '__main__':
    sol = Solution()
    sol.maxMulti([-2, 0, -1])
