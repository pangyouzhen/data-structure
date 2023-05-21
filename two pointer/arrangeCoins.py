import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(math.sqrt(1 + 4 * n) / 2) - 1
