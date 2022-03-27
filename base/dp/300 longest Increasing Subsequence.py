# dp[x] = max(dp[x], dp[y] + 1) 其中 y < x 并且 nums[x] > nums[y]

class Solution:
    def lengthOfLIS(self, nums):
        size = len(nums)
        dp = [1] * size
        for i in range(size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(f"{dp =}")
        return max(dp) if dp else 0
        
    # TODO why error  
    def lengthOfLIS2(self,nums):
        l = len(nums)
        dp = [1] * l
        for i in range(l):
            for j in range(1, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i-1],dp[j] + 1)
        print(f"{dp = }")
        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    print("---------------------")
    # print(sol.lengthOfLIS([50, 3, 10, 7, 40, 80]))
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [10, 2, 9, 3, 11, 5]
    # for i in range(1, len(nums)):
    #     print(nums[:i])
    #     print(sol.lengthOfLIS(nums[:i]))
    #     print("-------------------------")
    print(sol.lengthOfLIS(nums))
    print("********************")
    nums2 = [5, 6, 7, 1, 2]
    print(sol.lengthOfLIS(nums2))
    nums3 = [0,1,0,3,2,3]
    print(sol.lengthOfLIS(nums3))
    print(sol.lengthOfLIS2(nums3))
