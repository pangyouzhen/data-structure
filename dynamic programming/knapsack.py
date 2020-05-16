from typing import List

#  需要修改，有些问题
class Solution:
    def knapsack(self, N: int, W: int, wt: List[int], val: List[int]) -> int:
        # dp = [[] for i in range(N) for j in range(W)]
        dp = [[0] * W for i in range(N)]
        print(dp)
        for i in range(N):
            for w in range(W):
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
    W = 4[[0, 0, 0, 3], [0, 0, 4, 4], [0, 2, 4, 6]]

    #  书包总重量
    wt = [2, 1, 3]
    #  每个物品的重量
    val = [4, 2, 3]
    #  每个物品的价值'
    sol = Solution()
    print(sol.knapsack(N, W, wt, val))
