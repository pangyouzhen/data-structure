from typing import List
from collections import Counter


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        res = 0
        t = []
        for i in A:
            (odd, even) = self.nums_odd_even(i)
            odd = Counter(odd)
            even = Counter(even)
            if (odd, even) not in t:
                t.append((odd, even))
                res += 1
        return res

    def nums_odd_even(self, i):
        odd = []
        even = []
        for i, v in enumerate(i):
            if i % 2 == 0:
                even.append(v)
            else:
                odd.append(v)
        return (odd, even)


if __name__ == '__main__':
    nums = ["abc", "acb", "bac", "bca", "cab", "cba"]
    # ["abc", "cba"]，["acb", "bca"]，["bac", "cab"]
    # nums = ["abc", "cba"]
    sol = Solution()
    print(sol.numSpecialEquivGroups(nums))
