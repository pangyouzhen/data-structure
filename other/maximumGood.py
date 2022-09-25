from typing import List

# TODO
class Solution:
    def maximumGood(self, nums: List[List[int]]) ->int:
        l = len(nums)
        cols = [[]] * l
        for i in range(l):
            for j in nums:
                cols[i].append(j[i])
        print(cols)
        

if __name__ =="__main__":
    func = Solution().maximumGood
    nums =[]
    print(func(nums))