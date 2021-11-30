from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ls = text.split()
        res = []
        for i in range(len(ls) - 2):
            if ls[i] == first and ls[i + 1] == second:
                #  注意这里的list的append和+= 是不一样的
                res.append(ls[i + 2])
        return res


