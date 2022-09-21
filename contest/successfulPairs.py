from bisect import bisect
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort(reverse=True)
        p = [success / i for i in potions]
        l = len(spells)
        res = []
        print(p)
        for j in spells:
            t = bisect(p, j)
            res.append(t)
        return res


if __name__ == "__main__":
    func = Solution().successfulPairs
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    print(func(spells, potions, success))
