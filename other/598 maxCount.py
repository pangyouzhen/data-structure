from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # 暴力解法会超时
        # l = len(ops)
        # matrix = [[0] * m for i in range(n)]
        # while l > 0:
        #     op = ops[-l]
        #     for i in range(op[0]):
        #         for j in range(op[1]):
        #             matrix[i][j] = matrix[i][j] + 1
        #     l -= 1
        # 这里用 两层循环是不合适d的40000 * 40000 = 16 * 10^8
        # res = [j for i in matrix for j in i]
        # fst = sorted(res, reverse=True)[0]
        # return res.count(fst)
        if not ops:
            return m * n
        fst, second = ops[0][0], ops[0][1]
        for f, s in ops[1:]:
            if f < fst:
                fst = f
            if s < second:
                second = s
        return fst * second


if __name__ == '__main__':
    func = Solution().maxCount
    m = 40000
    n = 40000
    operations = []
    print(func(m, n, operations))
