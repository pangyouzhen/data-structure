from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int):
        l = len(customers)
        val = float("-inf")
        res = 0
        for i, j in zip(customers, grumpy):
            if j == 0:
                res += i
        for i in range(l - minutes + 1):
            temp = 0
            for c, g in zip(customers[i:i + minutes], grumpy[i:i + minutes]):
                # 1 是生气
                if g == 1:
                    temp += c
            if temp > val:
                val = temp
        return res + val


if __name__ == '__main__':
    sol = Solution()
    # customers = [1, 0, 1, 2, 1, 1, 7, 5]
    # grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    # X = 3
    customers = [5, 8]
    grumpy = [0, 1]
    X = 1
    print(sol.maxSatisfied(customers, grumpy, X))
