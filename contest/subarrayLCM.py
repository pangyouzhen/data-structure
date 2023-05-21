# from math import lcm
from typing import List
import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

class Solution:
    # timeout
    def subarrayLCM2(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums) + 1):
                if len(nums[i:j]) == 1:
                    if nums[i:j][0] == k:
                        ans += 1
                elif nums[i:j] and lcm(*nums[i:j]) == k:
                    ans += 1
        return ans

    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            LCM = 1
            for j in range(i,n):
                print(i,j)
                LCM = lcm(LCM,nums[j])
                if k % LCM: break
                if LCM == k:
                    ans += 1
        return ans

if __name__ == '__main__':
    func = Solution().subarrayLCM
    #nums = [3,5,3,3,2]
    nums = [3,6,2,7,1]
    k =6 
    print(func(nums, k))
