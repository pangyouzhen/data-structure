class Solution:
    def maxProfit(self, prices):
        res = []
        i = 0
        while (i < len(prices) - 1):
            if (prices[i + 1] > prices[i]):
                res.append(prices[i + 1] - prices[i])
            i = i + 1
        return sum(res)
