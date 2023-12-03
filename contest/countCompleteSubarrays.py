from collections import Counter
from typing import List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        k = len(set(nums))
        cnt = Counter(nums[:k - 1])
        print(cnt)
        for in_, out in zip(nums[k - 1:], nums):
            cnt[in_] += 1
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]
            if len(cnt) == k:
                ans += 1
        return ans

if __name__ == "__main__":
    func = Solution().countCompleteSubarrays
    nums = [1,3,1,2,2]
    print(func(nums))