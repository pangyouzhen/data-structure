from typing import List

import pysnooper


class Solution:
    @pysnooper.snoop()
    def maximumNumber(self, num: str, change: List[int]) -> str:
        res = ""
        queue = []
        for i, v in enumerate(num):
            a = (change[int(v)])
            if a > int(v):
                res += str(a)
                queue.append(True)
            #     True 代表替换比原始值大
            elif a < int(v):
                res += v
                queue.append(False)
            else:
                res += v
            if len(set(queue)) > 1:
                res += num[i + 1:]
                break
            while queue and queue[0] is False:
                queue.pop(0)
        # print(res)
        return res

if __name__ == '__main__':
    # 可以视为 一个滑动的窗口，F，F，T的情况前面就直接舍弃 + 双指针
    func = Solution().maximumNumber
    # T,F,T
    assert func("132", [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]) == "832"
    # T,T,T
    assert func("021", [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]) == "934"
    # F
    assert func("5", [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]) == "5"
    # F,F,F,T,T,T
    assert func("334111", [0, 9, 2, 3, 3, 2, 5, 5, 5, 5]) == "334999"
    # T,T,T,
    assert func("214010", [6, 7, 9, 7, 4, 0, 3, 4, 4, 7]) == "974676"
