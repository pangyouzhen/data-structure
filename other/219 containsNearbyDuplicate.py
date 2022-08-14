from typing import List
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)
        for i,v in enumerate(nums):
            d[v].append(i)
            if len(d[v]) > 1:
                if d[v][-1] - d[v][-2] <= k:
                    return True
        return False
        

if __name__ == '__main__':
    nums = [1, 0, 1, 1]
    k = 1
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))
