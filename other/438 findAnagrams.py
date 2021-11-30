from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        temp = list(s)
        a = 1
        l_s = len(temp)
        l_p = len(p)
        _ = temp[:l_p]
        c = Counter(_)
        temp_p = Counter(p)
        while a < (l_s - l_p + 1):

            res.append(a)
        a += 1
        return res


if __name__ == '__main__':
    # s = "cbaebabacd"
    # p = "abc"
    s = "ababababab"
    p = "aab"
    func = Solution().findAnagrams
    print(func(s, p))
