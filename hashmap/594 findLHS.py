from typing import List
from collections import Counter, defaultdict

# 字典
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        a = defaultdict(int)
        for k, v in c.items():
            _ = k - 1
            if _ in c.keys():
                a[k] = c[_] + c[k]
            else:
                a[k] = 0
        val = a.values()
        return max(val)


if __name__ == '__main__':
    # nums = [1, 3, 2, 2, 5, 2, 3, 7]
    # nums = [1, 1, 1, 1]
    nums = [1, 2, 3, 4]
    sol = Solution()
    print(sol.findLHS(nums))
