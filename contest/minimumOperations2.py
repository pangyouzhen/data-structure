from itertools import combinations

class Solution:
    def minimumOperations(self, num: str) -> int:
        if int(num) % 5 == 0:
            return 0
        for i in range(1,len(num)):
            for j in combinations(num,len(num)-i ):
                val = int("".join(j))
                if val % 25 == 0:
                    return i