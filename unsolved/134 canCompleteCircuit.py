from typing import List


class Solution:
    #  暴力解法 超时
    def canCompleteCircuit_(self, gas: List[int], cost: List[int]) -> int:
        inds = []
        l = len(gas)
        # 初始的k值，排除一开始就不够的
        for k, (i, v) in enumerate(zip(gas, cost)):
            if i >= v:
                inds.append(k)
        for ind in inds:
            # 从3开始
            ms = [i for i in range(l)]
            t = ms[ind:l] + ms[0:ind]
            res = 0
            for i in t:
                res += gas[i]
                res -= cost[i]
                if res < 0:
                    break
            if res >= 0:
                return ind
        return -1

    # todo
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        pass


if __name__ == '__main__':
    func = Solution().canCompleteCircuit
    # gas = [1, 2, 3, 4, 5]
    # cost = [3, 4, 5, 1, 2]
    # gas = [2, 3, 4]
    # cost = [3, 4, 3]
    gas = [2]
    cost = [2]
    print(func(gas, cost))
