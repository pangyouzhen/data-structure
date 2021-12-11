from typing import List


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        l = len(nums)
        res = 0
        for i in range(l):
            for j in range(i + 1, l):
                if abs(nums[j] - nums[i]) == k:
                    res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 2, 1]
    k = 1
    print(sol.countKDifference(nums, k))
