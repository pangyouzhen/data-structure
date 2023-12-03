from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        s = []
        max_ = nums[0]
        i = 0
        res = 0
        while i < len(nums):
            if abs(nums[i] - max_) <3:
                s.append(nums[i])
            else:
                l = len(s)
                res += int((l+1)*l/2)
                s = s[1:]
            i += 1
        l = len(s)
        res += int((l+1)*l/2)
        return res

if __name__ == "__main__":
    func = Solution().continuousSubarrays
    nums = [5,4,2,4]
    print(func(nums))