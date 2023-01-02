from typing import List
from math import pow


class Solution:
    def longestSquareStreak2(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        dp = [1] * l
        for i in range(l):
            for j in range(i):
                if nums[i] == nums[j] ** 2:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        while nums:
            t = 1
            m = max(nums)
            val = pow(m, 1 / 2)
            int_val = int(val)
            nums -= {m}
            while int_val == val and int_val in nums:
                nums -= {val}
                val = pow(val, 1 / 2)
                int_val = int(val)
                t += 1
            res = max(t, res)
        if res == 1:
            return -1
        return res


if __name__ == "__main__":
    func = Solution().longestSquareStreak
    nums = [4, 3, 6, 16, 8, 2]
    print(func(nums))
