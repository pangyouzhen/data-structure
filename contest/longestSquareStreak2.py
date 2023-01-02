from typing import List
from math import pow


class Solution:
    def longestSquareStreak2(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        while nums:
            n = 1
            m = max(nums)
            val = pow(m, 1 / 2)
            int_val = int(val)
            nums -= {m}
            while int_val == val and int_val in nums:
                nums -= {int_val}
                val = pow(val, 1 / 2)
                int_val = int(val)
                n += 1
            ans = max(ans, n)
        if ans == 1:
            return -1
        return ans


if __name__ == "__main__":
    func = Solution().longestSquareStreak
    nums = [4, 3, 6, 16, 8, 2]
    print(func(nums))
