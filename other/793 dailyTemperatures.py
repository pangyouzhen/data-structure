from typing import List


# 超时
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    sol = Solution()
    print(sol.dailyTemperatures(temperatures))
    temperatures2 = [55, 38, 53, 81, 61, 93, 97, 32, 43, 78]
    sol = Solution()
    print(sol.dailyTemperatures(temperatures2))
