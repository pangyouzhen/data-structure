from typing import List
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ws = [i[0] for i in words]
        w = "".join(ws)
        if s == w:
            return True
        else:
            return False