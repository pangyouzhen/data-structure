from typing import List
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        c = Counter(nums)
        for i, v in c.items():
            if v == 2:
                res.append(i)
        a = (i for i in range(1, len(nums) + 1))
        res.extend(list((set(a) ^ set(c.keys()))))
        return res


if __name__ == '__main__':
    nums = [3, 2, 3, 4, 6, 5]
    sol = Solution()
    print(sol.findErrorNums(nums))
