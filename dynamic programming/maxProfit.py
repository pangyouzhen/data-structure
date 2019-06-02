class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        res = []
        for i in range(0, len(prices)):
            if i == 0:
                res.append([prices[0]])
            elif prices[i] <= prices[i - 1]:
                res.append([prices[i]])
            else:
                len_res = len(res)
                for t in range(1, len_res + 1):
                    if prices[i] > res[-t][-1]:
                        res[-t].append(prices[i])
        _ = list(filter(lambda x: len(x) >= 2, res))
        if len(_) == 0:
            return 0
        minus = list(map(lambda x: x[-1] - x[0], _))
        return max(minus)


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
