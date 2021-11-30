from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        for i in range(len(prices) - 1):
            temp = prices[i + 1] - prices[i]
            if temp > 0:
                res.append(temp)
        return sum(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
    print(sol.maxProfit([1, 2, 3, 4, 5]))
    print(sol.maxProfit([7, 6, 4, 3, 1]))
