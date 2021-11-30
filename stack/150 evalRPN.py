from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = ["+", "-", "*", "/"]
        stack = []
        for i in tokens:
            if i in a:
                val = int(eval(stack[-2] + i + stack[-1]))
                stack.pop(-1)
                stack.pop(-1)
                stack.append(str(val))
            else:
                stack.append(i)
        return int(stack[0])


if __name__ == '__main__':
    nums = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    # nums = ["2", "1", "+", "3", "*"]
    # nums = ["4", "13", "5", "/", "+"]
    sol = Solution()
    print(sol.evalRPN(nums))
