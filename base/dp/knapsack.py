from typing import List


#  需要修改，有些问题
#  背包问题，从顶层到底层进行递归
# 状态转移方程 F(i,c) = max(F(i-1,c) ,v(i) + F(i-1,c-w(i)))
# TODO
class Solution:
    def knapsack(self, N: int, W: int, wt: List[int], val: List[int]) -> int:
        # dp = [[] for i in range(N) for j in range(W)]
        dp = [[0] * (W + 1) for i in range(N + 1)]
        # print(dp)
        for i in range(1, N + 1):
            for w in range(1, W + 1):
                if w - wt[i - 1] < 0:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(
                        dp[i - 1][w],
                        val[i - 1] + dp[i - 1][w - wt[i - 1]])
        # print(dp)
        return dp[N][W]


# C 背包的容量，w 每件物品的重量，
class Solutions:
    def __init__(self):
        self.memo = None

    def knapsack01(self, w: List[int], v: List[int], c: int):
        n = len(w)
        self.memo = [[-1] * (c + 1) for _ in range(n)]
        result = self.bestValue(w, v, n - 1, c)
        return result
    #  用1，...index 的物品填充 容量为c的物品

    def bestValue(self, w: List[int], v: List[int], index: int, c: int):
        if index < 0 or c <= 0:
            return 0
        # 解决重叠子问题
        if self.memo[index][c] != -1:
            return self.memo[index][c]
        res = self.bestValue(w, v, index - 1, c)
        if c >= w[index]:
            res = max(res,
                      v[index] + self.bestValue(w, v, index - 1, c - w[index]))
        # 这里还有重叠子问题的情况
        self.memo[index][c] = res
        return res


if __name__ == '__main__':
    N = 3
    # N 个物品
    C = 100
    #  书包总重量
    # wt = [2, 1, 3]
    wt = [20,30,40,50,60]
    #  每个物品的重量
    # val = [4, 2, 3]
    val = [20,30,44,55,60]
    #  每个物品的价值'
    sol = Solution()
    print(sol.knapsack(N, C, wt, val))
    print("------------------------")
    sols = Solutions()
    print(sols.knapsack01(wt, val, C))
