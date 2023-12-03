from typing import List


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        res = 0
        all_nums = self.extract_group(nums,threshold)
        for nums in all_nums:
            l = 0
            r = len(nums)
            while l < r:
                if self.is_valid_group(nums[l:r],threshold):
                    res = max(res,len(nums[l:r]))
                else:
                    l += 1
        return res
                
                
    def extract_group(self,nums: List[int],threshold: int) ->List[List[int]]:
        ind = [i for i,v in enumerate(nums) if v > threshold]
        # 进行分组，切割成小于threshold的n个组
        all_nums = []
        if ind:
            ind.insert(0,0)
            for i in range(len(ind) - 1):
                all_nums.append(nums[i:i+1])
        else:
            all_nums.append(nums)
        return all_nums
    
    def is_valid_group(self,nums: List[int],threshold: int) -> bool:
        res = True
        for i,v in enumerate(nums):
            # 奇数索引
            if i % 2 ==0 and v % 2 !=0:
                return False
            # 偶数索引
            if i % 2!= 0 and v %2 ==0:
                return False
        return res