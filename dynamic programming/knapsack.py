from typing import List


#  需要修改，有些问题
#  背包问题，从顶层到底层进行递归
class Solution:
    def knapsack(self, N: int, W: int, wt: List[int], val: List[int]) -> int:
        # dp = [[] for i in range(N) for j in range(W)]
        dp = [[0] * (W + 1) for i in range(N + 1)]
        print(dp)
        for i in range(1, N + 1):
            for w in range(1, W + 1):
                if w - wt[i - 1] < 0:
                    dp[i][w] = dp[i - 1][w]
                else:
                    dp[i][w] = max(
                        dp[i - 1][w],
                        val[i - 1] + dp[i - 1][w - wt[i - 1]])
        print(dp)
        return dp[N][W]


if __name__ == '__main__':
    N = 3
    # N 个物品
    W = 3
    #  书包总重量
    # wt = [2, 1, 3]
    wt = [4, 3, 1]
    #  每个物品的重量
    # val = [4, 2, 3]
    val = [3000, 2000, 1500]
    #  每个物品的价值'
    sol = Solution()
    print(sol.knapsack(N, W, wt, val))
