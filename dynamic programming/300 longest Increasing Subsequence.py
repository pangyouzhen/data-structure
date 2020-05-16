# dp[x] = max(dp[x], dp[y] + 1) 其中 y < x 并且 nums[x] > nums[y]

class Solution:
    def lengthOfLIS(self, nums):
        size = len(nums)
        dp = [1] * size
        for x in range(size):
            for y in range(x):
                if nums[x] > nums[y]:
                    print(x,y)
                    print(nums[x],nums[y])
                    print("-----------")
                    dp[x] = max(dp[x], dp[y] + 1)
        return max(dp) if dp else 0


# ?????
class Solution2(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = (low + high) / 2
                if dp[mid] >= nums[x]:
                    high = mid - 1
                else:
                    low = mid + 1
            if low >= len(dp):
                dp.append(nums[x])
            else:
                dp[low] = nums[x]
        return len(dp)

if __name__ == '__main__':
    sol = Solution()
    print("---------------------")
    print(sol.lengthOfLIS([50, 3, 10, 7, 40, 80]))
