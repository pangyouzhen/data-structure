from typing import List
from functools import lru_cache
class Solution:
    def getDescentPeriods(self, nums: List) -> int:
        l = len(nums)
        dp = [1] * l
        t = []
        res = 0
        for i in range(1,l):
            if nums[i] - nums[i-1] == -1:
                dp[i] = dp[i-1] + 1 
            else:
                t.append(dp[i-1])
        t.append(dp[-1])
        for j in t:
            res += self.slice_window(j)
        return int(res)

    @lru_cache
    def slice_window(self,j:int):
        return (j+1)* j / 2 
        

if __name__ =="__main__":
    func = Solution().getDescentPeriods
    prices =[3,2,1,0]
    # prices = [8,6,7,7]
    print(func(prices))
