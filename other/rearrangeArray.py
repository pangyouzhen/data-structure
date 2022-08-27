from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        bigger_zero = []
        smaller_zero = []
        for i in nums:
            if i > 0:
                bigger_zero.append(i)
            else:
                smaller_zero.append(i)
        res=[]
        for i,v in zip(bigger_zero,smaller_zero):
            res.append(i)
            res.append(v)
        return res
            

if __name__ =="__main__":
    func = Solution().rearrangeArray
    nums =[]
    print(func(nums))