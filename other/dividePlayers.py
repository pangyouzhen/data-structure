from typing import List
from collections import Counter

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s = sum(skill)
        l = len(skill)
        if l % 2 != 0:
            return -1
        q,v = divmod(s,l / 2)
        if v != 0:
            return -1
        res = 0
        # c = Counter(skill)
        # for i,v in c.items():
        #     if c.get(q-i) and v > 0:
        #         c[q-i] -= 1
        #         c[i] -=1 
        #         res += i * (q-i) 
        #     else:
        #         return -1
        # return res
        ss = sorted(skill)
        start = 0
        end = len(ss) -1
        while start < end:
            if ss[start] + ss[end] == q:
                res += ss[start] * ss[end]
                start += 1
                end -= 1
            else:
                return -1
        return res
# RuntimeError: dictionary changed size during iteration
if __name__ == "__main__":
    func = Solution().dividePlayers
    skill = [3,2,5,1,3,4]
    print(func(skill))