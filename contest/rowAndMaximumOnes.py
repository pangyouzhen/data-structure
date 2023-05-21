from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_one = 0
        min_index = 0
        for i,v in enumerate(mat):
            one = v.count(1)
            if one > max_one:
                max_one = one
                min_index = i
        return [min_index,max_one]