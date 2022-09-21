from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        l = len(nums)
        max_val = -1
        for i in range(l):
            for j in range(i+1,l):
                print(i,j)
                if nums[j] - nums[i] > 0:
                     max_val = max(nums[j] - nums[i],max_val)
        return max_val

if __name__ =="__main__":
    func = Solution().maximumDifference
    nums =[7,1,5,4]
    print(func(nums))