from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for i in A:
            res.append(i[::-1])
        for i, v in enumerate(res):
            for j in v:
                if j == 1:
                    res[i][j] = 0
                else:
                    res[i][j] = 1
        return res
