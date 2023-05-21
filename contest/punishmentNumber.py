from itertools import combinations
from typing import List


class Solution:
    def punishmentNumber(self, n: int) -> int:
        res: list[int] = []
        for i in range(1, n+1):
            square = str(int(i * i))
            t = len(square)
            sum_ = i
            one_ans: List[int] = []
            if self.punishmentNumberi(square, one_ans, t, sum_):
                res.append(int(square))
        return sum(res)

    def punishmentNumberi(self, s: str, one_ans, t, sum_) -> bool:
        if not s:
            if sum(one_ans) == sum_:
                return True
            return False
        for i in range(t):
            one_ans.append(int(s[i]))
            self.punishmentNumberi(s[i+1:], one_ans, len(s), sum_)
            one_ans.pop()


if __name__ == "__main__":
    sol = Solution()
    func = sol.punishmentNumber
    func2 = sol.punishmentNumberi
    s = "1296"
    one_ans = []
    t = len(s)
    sum_ = 36
    # print(func(10))
    print(func2(s,one_ans,t,sum_))
