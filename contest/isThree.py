import math


class Solution:
    def isThree(self, n: int) -> bool:
        if n < 3:
            return False
        res_ls = []
        for i in range(2, n):
            res = n / i
            if int(res) == res and res != i:
                return False
            elif int(res) == res and res == i:
                res_ls.append(res)
            else:
                continue
        if len(res_ls) == 1:
            return True
        return False


if __name__ == '__main__':
    func = Solution().isThree
    assert func(4) is True
    assert func(81) is False
    assert func(14) is False
    assert func(2) is False
    assert func(13) is False
