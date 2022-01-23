from typing import List
from collections import Counter

class Solution():
    def countElements(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        if max_val == min_val:
            return 0
        c = Counter(nums)
        return len(nums) - c[min_val] - c[max_val] 
             

if __name__ =="__main__":
    func = Solution().countElements
    nums =[-89,39,39,-89,39,39]
    print(func(nums))