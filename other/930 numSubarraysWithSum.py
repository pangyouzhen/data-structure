from typing import List
from collections import Counter

# todo
#  滑动窗口问题
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        s = sum(nums)
        if s < goal:
            return 0
        c = Counter(nums)
        pass


if __name__ == '__main__':
    sol = Solution()
