import re
from string import ascii_lowercase
from typing import List

from pysnooper import snoop


class Solution:
    #  todo 怎样切分看下更好
    def __init__(self):
        self.vowels = {'a', "e", 'i', 'o', 'u'}

    def countVowelSubstrings(self, word: str) -> int:
        lowercase = set(ascii_lowercase) - self.vowels
        print(lowercase)
        pattern = re.compile(f"[{list(lowercase)}]")
        w: List[str] = re.split(pattern, word)
        res = 0
        for j in w:
            res += self.get_number(j)
        return res

    @snoop()
    def get_number(self, w: str):
        t = 0
        start = 0
        end = len(w)
        for i in range(len(w)):
            if set(set(w[i:])):
                pass


if __name__ == '__main__':
    func = Solution().countVowelSubstrings
    func2 = Solution().get_number
    print(func2("uaieuoua"))
