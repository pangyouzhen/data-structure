from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        l = len(nums)
        res = 0
        for i in range(l-2):
            for j in range(i+1,l-1):
                for k in range(j+1,l):
                    v = (nums[i] - nums[j]) * nums[k]
                    res = max(res,v)
        return res
    
if __name__ == "__main__":
    func = Solution().maximumTripletValue
    nums = [10,13,6,2]
    print(func(nums))
    