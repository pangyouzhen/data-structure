from typing import List
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        all_index = defaultdict(list)
        for i,v in enumerate(nums):
            all_index[v].append(i)
            if len(all_index[v]) >= 2:
                if i - all_index[v][-2] <= k:
                    return True
        return False

if __name__ == '__main__':
    nums = [1,2,3,1,2,3]
    k = 2
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums, k))
