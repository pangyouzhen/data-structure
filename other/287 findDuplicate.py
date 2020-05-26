import collections
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            if i not in a:
                a[i] = 0
            else:
                return i


if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicate([1,3,4,2,2]))