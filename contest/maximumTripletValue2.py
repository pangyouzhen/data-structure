from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        all_nums = [(i,v) for i,v in enumerate(nums)]
        all_nums.sort(lambda x:x[1])
        # 3个指针 fst,second,thrid
        
        while second > fst:
            pass