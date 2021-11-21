from array import array
from utils import register
from collections import defaultdict
from typing import List


@register.register
# todo
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arrs = defaultdict(list)
        for i, v in enumerate(arr):
            self.arrs[v].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value in self.arrs.keys():
            inds = self.arrs[value]
            left_ind = 0
            right_ind = len(inds) - 1
            while left_ind <= right_ind:
                if inds[left_ind] < left:
                    left_ind += 1
                if inds[right_ind] > right:
                    right_ind -= 1
                if inds[left_ind] >= left and inds[right_ind] <= right:
                    return right_ind - left_ind + 1
        return 0


if __name__ == '__main__':
    # Your RangeFreqQuery object will be instantiated and called as such:
    # obj = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
    # param_1 = obj.query(1, 2, 4)
    # print(param_1)
    # print(obj.query(0, 11, 33))
    func = ["RangeFreqQuery", "query", "query", "query", "query", "query", "query"]
    input_array = [[[8, 4, 2, 5, 4, 5, 8, 6, 2, 3]], [0, 3, 5], [5, 6, 2], [6, 8, 4], [2, 8, 3], [4, 5, 1], [2, 4, 2]]
