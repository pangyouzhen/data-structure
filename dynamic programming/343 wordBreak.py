class Solution:
    def integerBreak(self, n: int) -> int:
        #     状态转移方程
        #  动态规划的本质是什么，本质是递归，但是递归的过程中有重叠的子问题，从顶往下是递归，从底网上是动态规划
        #  能够求出子问题的最优解，想一下fib序列
        # memo = [-1] * (n+1)
        # if n == 1:
        #     return 1
        # if memo[n] != -1:
        #     return memo[n]
        # res = -1
        # for i in range(1, n):
        #     res = max(res, i * (n - i), i * self.integerBreak(n - i))
        # memo[n] = res
        # return res

        dp = [-1] * (n + 1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        print(dp)
        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    print(sol.integerBreak(10))
    print(sol.integerBreak(9))
    print(sol.integerBreak(25))
