from collections import Counter


class Solution:
    def countSubarrays1(self, nums: List[int], k: int) -> int:
        m = max(nums)
        l = len(nums)
        res = 0
        for i in range(l):
            for j in range(i, l):
                c = Counter(nums[i:j])
                if c[m] >= k:
                    res += 1
        return res
        
    def countMaxSubarrays(self,nums, k):
        left, right, max_count, count, result = 0, 0, 0, collections.Counter(), 0
        for right, num in enumerate(nums):
            count[num] += 1
            max_count = max(max_count, count[num])
            while max_count >= k:
                if right - left + 1 >= k:
                    result += right - left + 1
                count[nums[left]] -= 1
                max_count = max(count.values())
                left += 1
        return result

    def countSubarrays2(self, nums: List[int], k: int) -> int:
        m = max(nums)
        l = len(nums)
        res = 0
        c = Counter(nums)
        for in_,out in zip(nums,nums):
            c[in_] += 1
            if c
        return res

            
