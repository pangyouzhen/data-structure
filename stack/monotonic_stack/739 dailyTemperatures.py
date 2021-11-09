from typing import List
from pysnooper import snoop


class Solution:
    # @snoop()
    # 暴力解法
    def dailyTemperatures_(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        l = len(temperatures)
        res = [0] * l
        for i in range(l):
            for j in range(i + 1, l):
                if temperatures[j] > temperatures[i]:
                    print(f"{temperatures[j]} > {temperatures[i]}")
                    res[i] = j - i
                    break
        return res

    # 单调栈应用场景: 每个数右边第一个比它大的数
    @snoop()
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        ans = [0] * l
        stack = []
        for i in range(l):
            temperature = temperatures[i]
            while stack and temperature > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans

    # 单调栈这里改成如果得到的是值怎么改
    # todo
    def dailyTemperatures_value(self, temperatures: List[int]) -> List[int]:
        pass


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    # temperatures = [30, 40, 50, 60]
    # temperatures = [30, 60, 90]
    func = Solution().dailyTemperatures
    print(func(temperatures))
