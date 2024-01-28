from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        b = bin(n)
        b = b[2:]
        even = 0
        odd = 0
        for i,v in enumerate(b):
            if i % 2 ==0 and v == "1":
                even += 1
            elif i % 2 == 1 and v == "1":
                odd += 1
        return [even,odd]

n = 2
func = Solution().evenOddBit
print(func(2))