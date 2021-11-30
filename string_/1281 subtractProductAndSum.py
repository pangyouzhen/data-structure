from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_n = str(n)
        ls = [int(i) for i in list(str_n)]
        mul_ = reduce(lambda x, y: x * y, ls)
        sum_ = sum(ls)
        return mul_ - sum_
