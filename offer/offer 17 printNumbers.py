from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        nums =int( n * "9")
        return [i for i in range(1,nums + 1)]
