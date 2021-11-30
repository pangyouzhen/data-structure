from typing import List
import pysnooper


class Solution:
    @pysnooper.snoop()
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        res = 0
        for i in nums:
            if i == 1:
                curr += 1
            else:
                if curr > res:
                    res = curr
                curr = 0
        return max(res, curr)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
