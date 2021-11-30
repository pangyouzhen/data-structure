from typing import List
from pprint import pprint

a = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]


#
# for i in range(3):
#     a[2][i] += min(a[3][i], a[3][i + 1])
#
# print(a[2])
#
# for i in range(2):
#     a[1][i] += min(a[2][i], a[2][i + 1])
# print(a[1])
#
# for i in range(1):
#     a[0][0] += min(a[1][i], a[1][i + 1])
# print(a)


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #  从题目中得知，对于节点(i,j) 的上一层的相邻节点是(i-1,j) 和 (i-1,j-1)
        #  所以 状态转移方程式就是 f(i,j) = min(f(i-1,j),f(i-1,j-1)) + triangle(i,j)， 这样就得出最后一行，取最小值就OK
        n = len(triangle)
        f = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            f[0][i] = triangle[0][0]

        for i in range(1, n):
            for j in range(n):
                if j >= len(triangle[i]):
                    # 这里有问题
                    f[i][j] = f[i][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]) + triangle[i][j]
        pprint(f)
        # dp = [
        # [2, 0, 0, 0],
        # [5, 6, 0, 0],
        # [11, 10, 13, 0],
        # [15, 11, 18, 16]]
        return min(f[- 1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTotal(a))
    b = [[-1], [2, 3], [1, -1, -3]]
    print(sol.minimumTotal(b))
    c = [[-1], [3, 2], [-3, 1, -1]]
    print(sol.minimumTotal(c))
