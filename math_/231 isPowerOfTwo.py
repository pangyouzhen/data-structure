import math


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            x = math.log2(n)
        return (math.ceil(x) == math.floor(x))
