from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res = []
        for i in matrix:
            min_val = min(i)
            min_index = i.index(min_val)
            max_val = max(map(lambda x: x[min_index], matrix))
            if min_val == max_val:
                res.append(min_val)
        return res
