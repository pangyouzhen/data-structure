from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = ["+", "-", "*", "/"]
        nums_list = []
        for i in tokens:
            if i in a:
                temp = 0
                if i == "+":
                    temp = sum(nums_list[-2:])
                elif i == "-":
                    temp = nums_list[-2] - nums_list[-1]
                elif i == "*":
                    temp = nums_list[-2] * nums_list[-1]
                elif i == "/":
                    temp = int(nums_list[-2] / nums_list[-1])
                del nums_list[-2:]
                nums_list.append(temp)
                print(nums_list)
            else:
                nums_list.append(int(i))
                print(nums_list)
        return nums_list[-1]


if __name__ == '__main__':
    nums = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    # nums = ["2", "1", "+", "3", "*"]
    # nums = ["4", "13", "5", "/", "+"]
    sol = Solution()
    print(sol.evalRPN(nums))
