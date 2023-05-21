import math


class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        k1_k2 = endPos + k - startPos
        if k1_k2 < 0:
            return 0
        if k1_k2 % 2 == 1:
            return 0
        k1 = k1_k2 / 2
        k2 = k1_k2 - k1
        if k1 < 0 or k2 < 0:
            return 0
        print(k1, k2)
        res = math.comb(k, int(k1))
        return int(res % (10 ** 9 + 7))


if __name__ == '__main__':
    # startPos = 1
    # endPos = 2
    # k =3
    startPos = 989
    endPos = 1000
    k = 99
    func = Solution().numberOfWays
    # print(func(startPos, endPos, k))
    assert func(startPos, endPos, k) == 934081896
