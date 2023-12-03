from typing import List

# TODO
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        l = len(nums)
        dp = [0] * l
        dp[-1] = -1
        for i in range(l):
            for j in range(i+1,l):
                if abs(nums[i] - nums[j]) <= target:
                    dp[j] = max(dp[i]+1,dp[j])
        print(dp)
        return dp[-1]
        
if __name__ == "__main__":
    func = Solution().maximumJumps
    # nums = [1,3,6,4,1,2]
    # target = 2  
    # nums= [0,1,3,2]
    # target = 1
    nums= [0,2,1,3]
    target = 1
    print(func(nums,target))