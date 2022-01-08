from typing import List


class Solution:
    # todo
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l == 1:
            return 0
        elif l  == 2:
            return max(prices[1] - prices[0], 0)
        elif l == 3:
            return max(prices[2] - prices[1], prices[2]-prices[0], prices[1] - prices[0],0) 
        dp = [0] * l
        dp[1] = max(prices[1] - prices[0], 0)
        dp[2] = max(prices[2] - prices[1], prices[2]-prices[0], dp[1])
        for i in range(3, l):
            dp[i] = max(dp[i-1], dp[i-3]+prices[i]-prices[i-1])
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 0, 2]
    print(sol.maxProfit(nums))
