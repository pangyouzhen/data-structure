from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        a = 0
        for i in accounts:
            if sum(i) > a:
                a = sum(i)
        return a