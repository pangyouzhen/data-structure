from typing import List


class Solution:
    # 数学解法 
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        res = [0]
        for i, v in zip(gas, cost):
            last_val = res[-1] + i-v
            res.append(last_val)
        min_val = min(res)
        return res.index(min_val)


if __name__ == '__main__':
    func = Solution().canCompleteCircuit
    # gas = [1, 2, 3, 4, 5]
    # cost = [3, 4, 5, 1, 2]
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    # gas = [2]
    # cost = [2]
    print(func(gas, cost))
