from typing import List
from collections import defaultdict

class Solution():
    # todo
    def maximumInvitations(self, favorite: List) -> int:
        a = defaultdict(list)
        # 只有一个出度，统计入度即可
        for i,v in enumerate(favorite):
            a[v].append(i)
        res = 0
        for k,v in a.items:
            l = len(a[k])
            pass
                

if __name__ =="__main__":
    func = Solution().maximumInvitations
    nums =[]
    print(func(nums))