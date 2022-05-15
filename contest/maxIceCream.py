class Solution:
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        t = 0
        m = 0
        for i, v in enumerate(costs):
            t += v
            if t > coins:
                break
            m += 1
        return m


if __name__ == '__main__':
    # costs = [1, 3, 2, 4, 1]
    # coins = 7
    # costs = [10, 6, 8, 7, 7, 8]
    # coins = 5
    costs = [1, 6, 3, 1, 2, 5]
    coins = 20
    sol = Solution()
    print(sol.maxIceCream(costs, coins))
