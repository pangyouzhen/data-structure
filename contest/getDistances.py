from typing import List
from collections import defaultdict
from functools import lru_cache, reduce


class Solution:
    #TODO
    def getDistances(self, arr: List[int]) -> List[int]:
        arr_dic = defaultdict(list)
        new_dic = defaultdict(int)
        for i, v in enumerate(arr):
            arr_dic[v].append(i)
        for k, v in arr_dic.items():
            if len(v) == 1:
                new_dic[v] = 0
            elif len(v) == 2:
                new_dic[v] = abs(v[0] - v[1])
            else:
                new_dic[v] = sum(reduce(lambda x, y: y - x, v))
        for i,v in enumerate(arr):
            # if
            pass

    @lru_cache()
    def get_abs_number(self, i, j):
        return abs(i - j)


if __name__ == '__main__':
    func = Solution().getDistances
    arr = [2, 1, 3, 1, 2, 3, 3]
    print(func(arr))
