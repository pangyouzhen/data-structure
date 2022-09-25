from collections import Counter
from typing import List

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) == 0:
            return ""
        c = Counter(s)
        not_include_str = []
        for i in c.keys():
            if i.lower() in c.keys() and i.upper() in c.keys:
                pass
        pass

if __name__ =="__main__":
    func = Solution().longestNiceSubstring
    nums =""
    print(func(nums))