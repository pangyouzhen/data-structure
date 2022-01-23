from typing import List
from collections import Counter
class Solution():
    def findLonely(self, nums: List) ->List[int] :
        c = Counter(nums)
        k = c.keys()
        res = []
        for i,v in c.items():
            if v == 1:
                if (i-1) not in k:
                    if (i+1) not in k:
                        res.append(i)
        return res

if __name__ =="__main__":
    func = Solution().findLonely
    nums =[]
    print(func(nums))