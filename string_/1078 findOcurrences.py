from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text_ls = text.split()
        res = []
        for i in range(len(text_ls) - 3 +1):
            if text_ls[i] == first and text_ls[i + 1] == second:
                res.append(text_ls[i + 2])
        return res


