from typing import List
import math

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        res = 0
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                if math.gcd(int(str(nums[i])[0]),int(str(nums[j])[-1])) == 1:
                    print(i,j)
                    res += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    func = sol.countBeautifulPairs
    assert func([31,25,72,79,74]) == 7