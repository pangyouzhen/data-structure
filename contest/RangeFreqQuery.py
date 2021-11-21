from bisect import bisect, bisect_left
from collections import defaultdict
from typing import List

from utils.Register import register


@register.register
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arrs = defaultdict(list)
        for i, v in enumerate(arr):
            self.arrs[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value in self.arrs.keys():
            inds = self.arrs[value]
            # bisect_right 表示相同值的右边，默认的是这个, insort 默认也是右边
            left_ind = bisect_left(inds, left)
            right_ind = bisect(inds, right)
            return right_ind - left_ind
        return 0


if __name__ == '__main__':
    # Your RangeFreqQuery object will be instantiated and called as such:
    obj = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
    # param_1 = obj.query(1, 2, 4)
    # print(param_1)
    # print(obj.query(0, 11, 33))
    # funcs = ["RangeFreqQuery", "query", "query", "query", "query", "query", "query"]
    # input_array = [[[8, 4, 2, 5, 4, 5, 8, 6, 2, 3]], [0, 3, 5], [5, 6, 2], [6, 8, 4], [2, 8, 3], [4, 5, 1], [2, 4, 2]]
    funcs = ["RangeFreqQuery", "query", "query"]
    input_array = [[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
    # funcs = ["RangeFreqQuery", "query", "query", "query"]
    # input_array = [[[2, 2, 1, 2, 2]], [2, 4, 1], [1, 3, 1], [0, 2, 1]]

    instances = None
    for i, v in zip(funcs, input_array):
        if i in register.keys():
            # 初始化class
            instances = register[i](*v)
        else:
            if instances and hasattr(instances, i):
                method = getattr(instances, i, None)
                if callable(method):
                    print(method(*v))
