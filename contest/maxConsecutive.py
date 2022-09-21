from typing import List
from bisect import bisect


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        res = [bottom, top]
        for i in special:
            bisect(res, i)
        print(res)


if __name__ == "__main__":
    func = Solution().maxConsecutive
