# time out
from typing import List
from functools import lru_cache


class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                s[i*i:n:i] = [0] * len(s[i*i:n:i])
        return sum(s)


if __name__ == '__main__':
    sol = Solution()

    print(sol.countPrimes(10))
    # 2 [2]
    # 3/2 [2,3]
    # 4/2 [2,3]
    # 5/2,5/3 [2,3,5]
    # 6/2 ---[]
    # 7/2,7/3,7/5 [2,3,5,7]
    # [2,3,4,5,6,7,8,9,10]
    assert sol.countPrimes(10) == 4
    assert sol.countPrimes(8) == 4
    # assert sol.countprimes(2) == 0
    # assert sol.countprimes(3) == 1
    res = sol.countPrimes(499979)
    print(res)
