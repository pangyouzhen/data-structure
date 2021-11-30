from typing import List
from collections import Counter

class Solution:
    def findDisappearedNumbers(self, nums):
        c = Counter(nums)
        n = len(nums)
        res = [i for i in range(1, n + 1) if i not in c.keys()]
        return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    sol = Solution()
    print(sol.findDisappearedNumbers(nums))
