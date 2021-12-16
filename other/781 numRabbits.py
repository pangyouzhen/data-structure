import math
from typing import List
from collections import Counter


class Solution:
    def numRabbits(self, answers: List[int]):
        res = 0
        c = Counter(answers)
        for k, v in c.items():
            if k <= v:
                color_number = math.ceil(v / (k + 1))
                res += color_number * (k + 1)
            else:
                res += k + 1
        return res


if __name__ == '__main__':
    # answers = [1, 0, 1, 0, 0]
    # answers = [10, 10, 10]
    answers = [1, 1, 2]
    sol = Solution()
    print(sol.numRabbits(answers))
