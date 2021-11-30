from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l = len(nums)
        if l <= k:
            return max(nums) - min(nums)
        nums.sort()
        res = []
        for i in range(l - k + 1):
            diff = nums[i + k - 1] - nums[i]
            res.append(diff)
        return min(res)


if __name__ == '__main__':
    sol = Solution().minimumDifference
    nums = [9, 4, 1, 7]
    k = 2
    print(sol(nums, k))
