from typing import List
import pysnooper


# todo
class Solution:
    @pysnooper.snoop()
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int):
        if minutes == len(customers) == len(grumpy):
            return sum(customers)
        right = 0
        window = []
        window2 = []
        res = 0
        all_sum = 0
        for i, v in zip(customers, grumpy):
            all_sum += i * v
        while right < len(grumpy):
            window.append(grumpy[right])
            window2.append(customers[right])
            right += 1
            if len(window) >= minutes:
                temp = 0
                for i, v in zip(window, window2):
                    if i == 0:
                        temp += v
                        val = all_sum + temp
                        if val > res:
                            res = val
        return res


if __name__ == '__main__':
    sol = Solution()
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3
    # customers = [5, 8]
    # grumpy = [0, 1]
    # X = 1
    print(sol.maxSatisfied(customers, grumpy, X))
