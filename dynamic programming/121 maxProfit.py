class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        mini = prices[0]
        maxi = prices[0]
        profit = 0
        for n in prices[1:]:
            if n < mini:
                mini = n
                maxi = n
            elif n > maxi:
                maxi = n
                profit = max(profit, maxi - mini)
        return profit


if __name__ == '__main__':
    sol = Solution()
    # assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 1]) == 0
    assert sol.maxProfit([7, 1, 5]) == 4
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([1, 2]) == 1
    assert sol.maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2
    assert sol.maxProfit([]) == 0
    assert sol.maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]) == 9
