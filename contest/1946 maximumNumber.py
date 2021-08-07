from typing import List

# import pysnooper


class Solution:
    # @pysnooper.snoop()
    def maximumNumber(self, num: str, change: List[int]) -> str:
        flag = 0
        n = len(num)
        nums = list(num)
        for i in range(n):
            if flag != -1:
                c = int(num[i])
                if c > change[c]:
                    if flag == 1:
                        flag = -1
                elif c < change[c]:
                    flag = 1
                    nums[i] = str(change[c])
        return "".join(nums)


# 这个题的两个关键点：
# 1. python的str是不可变的，需要生成list
# 2. 找到标识是变化的  flag=0表示没变 flag=1表示在变  flag=-1 表示变结束了

if __name__ == '__main__':
    func = Solution().maximumNumber
    assert func("132", [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]) == "832"
    assert func("021", [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]) == "934"
    assert func("5", [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]) == "5"
    assert func("334111", [0, 9, 2, 3, 3, 2, 5, 5, 5, 5]) == "334999"
    assert func("214010", [6, 7, 9, 7, 4, 0, 3, 4, 4, 7]) == "974676"
