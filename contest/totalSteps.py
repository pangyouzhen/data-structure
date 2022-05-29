from re import I
from typing import List
from functools import reduce

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        l = len(nums)
        start = 1
        while start < l and not self.is_not_mon(nums):
            if nums[start-1] > nums[start]:
                del nums[start]
                start -= 1
                l -= 1
            start += 1
        pass

    
    def is_not_mon(self,nums) -> bool:
        vals  = reduce(lambda x,y: x-y,nums)
        if min(vals) < 0:
            return False
        else:
            return True
        
if __name__ == "__main__":
    func = Solution().totalSteps
    # nums = [4,5,7,7,13]
    nums =[10,1,2,3,4,5,6,1,2,3]
    print(func(nums))
            