from typing import List


# todo
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int):
        if X == len(customers) == len(grumpy):
            return sum(customers)
        pass



if __name__ == '__main__':
    sol = Solution()
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy =    [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3
    print(sol.maxSatisfied(customers, grumpy, X))
