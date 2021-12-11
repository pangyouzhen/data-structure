from typing import List


class Solution:
    # 思路是对的，但是没剪枝，主要是双list没剪枝
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        total = sum(c for c, g in zip(customers, grumpy) if g == 0)
        maxIncrease = increase = sum(c * g for c, g in zip(customers[:minutes], grumpy[:minutes]))
        for i in range(minutes, n):
            increase += customers[i] * grumpy[i] - customers[i - minutes] * grumpy[i - minutes]
            maxIncrease = max(maxIncrease, increase)
        return total + maxIncrease



if __name__ == '__main__':
    sol = Solution()
    # customers = [1, 0, 1, 2, 1, 1, 7, 5]
    # grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    # X = 3
    customers = [5, 8]
    grumpy = [0, 1]
    X = 1
    print(sol.maxSatisfied(customers, grumpy, X))
