from typing import List
from itertools import combinations
from collections import Counter

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k == 0:
            return self.dfs(k,s,nums)
        return False
    
    def dfs(self,k,s,nums):
        if s < t:
            return False
        for i in range(len(nums)):
            for j in combinations(nums,i):
                if sum(j) == k:
                    s -= k
                    for t in j:
                        nums.remove(t)
                    self.dfs(k,s,l,nums)
        return True