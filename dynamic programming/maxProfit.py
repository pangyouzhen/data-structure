#


# M[i] = M[i - 1] + max((m[i] - m[i - 1]), 0)
class Solution:
    def maxProfit_memo(self, prices, M):
        pass
        # [7, 2] -> [0, 0, None]



    # ERROR
    #     max_value = prices[0]
    #     for i in range(1, len(prices)):
    #         if i == 1 and prices[1] > prices[0]:
    #             max_value = prices[1]
    #             M[2] = prices[1] - prices[0]
    #         elif i == 1 and prices[1] < prices[0]:
    #             max_value = prices[1]
    #             M[2] = 0
    #         elif prices[i] > max_value:
    #             minus = prices[i] - max_value
    #             max_value = prices[i]
    #             M[i + 1] = M[i] + minus
    #         else:
    #             M[i + 1] = M[i]
    #     return M[-1]
    #
    def maxProfit(self, prices):
        pass

        # ERROR
        # if len(prices) == 0 or len(prices) == 1:
        #     return 0
        # M = [None] * (len(prices) + 1)
        # M[0] = 0
        # M[1] = 0
        # # [7,2] ->  [0,0,None]
        # return self.maxProfit_memo(prices, M)


if __name__ == '__main__':
    sol = Solution()
    # assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 1]) == 0
    assert sol.maxProfit([7, 1, 5]) == 4
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([1, 2]) == 1
    assert sol.maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2
