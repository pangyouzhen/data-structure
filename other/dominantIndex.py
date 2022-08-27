from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        max_val = max(nums)
        max_ind = nums.index(max_val)
        for i,v in enumerate(nums):
            if i != max_ind:
                if max_val < (v*2):
                    max_ind = -1
                    break
        return max_ind

if __name__ =="__main__":
    func = Solution().dominantIndex
    nums =[1,2,3,4]
    print(func(nums))