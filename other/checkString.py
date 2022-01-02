from typing import List
from collections import defaultdict

class Solution():
    def checkString(self, s:str) -> bool:
        if not s:
            return True
        a = defaultdict(list)
        for i,v in enumerate(s):
            a[v].append(i)
        if not a["b"]:
            return True
        if a["a"]:
            ind_a = max(a["a"])
            ind_b = min(a["b"])
            if ind_b < ind_a:
                return False
        return True

if __name__ =="__main__":
    func = Solution().checkString
    nums= "aaa"
    print(func(nums))