from math import sqrt


def issquars(i):
    res = sqrt(i)
    if int(res) == res:
        return True
    return False


class Solution:
    def numSquares(self, n: int):
        if issquars(n):
            return 2
        memo = [float('inf')] * (n + 1)
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        #         memo[13] = memo[12] + 1 = memo[11] + 2 = ...= memo[9] + 4 = memo[8] + 5
        #         memo[12] = memo[11] + 1 = memo[10] + 2 = memo[9] + 3 = memo[8] + 4  = ... = memo[1] + memo[11]
        #         memo[0] = 0, memo[1] =1, memo[2] = 2,memo[3] = 3,
        #         memo[4] = min(memo[0] + 2^2, memo[3] + 1,memo[2] + 2,memo[1] + 3)  = 2 + 2 -> 2
        #         memo[5] = min(memo[0] + 5, memo[1] + 4, memo[2] + 3, memo[3] + 2, memo[4] + memo[1])
        #         memo[9] = min(memo[0] + 3^2, memo[1] + memo[8])
        if memo[n] != float("inf"):
            return memo[n]
        res = float("inf")
        for i in range(2, n):
            res = min(self.numSquares(i) + 1, res)
        memo[n] = res
        print(memo)
        return memo[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(5))
