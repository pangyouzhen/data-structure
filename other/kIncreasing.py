from math import floor
from typing import List


class Solution():
    def kIncreasing(self, nums: List[int], k: int) -> int:
        l = len(nums)
        group = floor(l / k)
        for j in range(group):
           for i in range(j, l, 3):
               print(nums[i])
        print("--------------")

if __name__ =="__main__":
    func = Solution().kIncreasing
    arr = [4,1,5,2,6,2]
    k = 2
    nums =[]
    print(func(arr,k))
