from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)
        ls = []
        for i in candies:
            if i + extraCandies >= max_:
                ls.append(True)
            else:
                ls.append(False)
        return ls