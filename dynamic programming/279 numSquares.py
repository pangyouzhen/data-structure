class Solution:
    def numSquares(self, n: int):
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # memo = [float('inf')] * (n + 1)
        #         memo[13] = memo[12] + memo[1] = memo[11] + memo[2] = ...= memo[9] + memo[4] = memo[8] + memo[5]
        #         memo[12] = memo[11] + memo[1] = memo[10] + memo[2] = memo[9] + memo[3] = memo[8] + memo[4] = ... = memo[1] + memo[11]
        #  memo[1] =1, memo[2] = 2,memo[3] = 3,memo[4] = 2^2  = 2 + 2 -> 2
        # if memo[n] != float("inf"):
        #     return memo[n]
        # res = float("inf")
        # for i in range(2, n):
        #     res = min(self.numSquares(i) + self.numSquares(n - i), res)
        # memo[n] = res
        # return memo[-1]
        pass


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(4))
