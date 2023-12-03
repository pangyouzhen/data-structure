from typing import List


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        # 考虑最终情况
        n = len(nums)
        return n <= 2 or any(nums[i]+nums[i+1] >= m for i in range(n-1))


if __name__ == "__main__":
    func = Solution().canSplitArray
    nums = [2, 1, 1, 3]
    m = 4
    print(func(nums, m))
