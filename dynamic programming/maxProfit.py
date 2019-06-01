#


# M[i] = M[i - 1] + max((m[i] - m[i - 1]), 0)
class Solution:
    def maxProfit_memo(self, prices, M):
        # [7, 2] -> [0, 0, None]
        for i in range(2, len(prices)):
            minus = prices[i] - prices[i - 1]
            if minus > 0:
                M[i] = M[i - 1] + minus
            else:
                M[i] = M[i - 1]
        return M[-1]

    def maxProfit(self, prices):
        if len(prices) == 0 or len(prices) == 1:
            return 0
        M = [None] * (len(prices))
        M[0] = 0
        M[1] = 0
        # [7,2] ->  [0,0,0]
        # [7,2] -> [None,None,None]
        return self.maxProfit_memo(prices, M)


if __name__ == '__main__':
    sol = Solution()
    # assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    res = sol.maxProfit([7, 1, 5, 3, 6, 4])
    print(res)
