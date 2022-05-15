from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        a = 0
        for word in words:
            if word.startswith(pref):
                a +=1
        return a