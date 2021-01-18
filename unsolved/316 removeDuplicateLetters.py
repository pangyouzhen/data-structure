from string import ascii_lowercase


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ascii_lowercase_dict = {v: i for i, v in enumerate(s)}
        res = ""
        for i,v in enumerate(s):
            if v not in res:
                res += v
