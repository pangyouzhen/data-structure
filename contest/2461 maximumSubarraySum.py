from collections import Counter
from typing import List


class Solution:
    # TODO 这里为啥时间复杂度超了？
    def maximumSubarraySum2(self, nums: List[int], k: int) -> int:
        l = len(nums)
        max_val = 0
        for i in range(l - k + 1):
            x = nums[i:i + k]
            if len(x) == len(set(x)):
                s = sum(x)
                if s > max_val:
                    max_val = s
        return max_val

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = Counter(nums[:k - 1])
        s = sum(nums[:k - 1])
        for in_, out in zip(nums[k - 1:], nums):
            cnt[in_] += 1
            s += in_
            if len(cnt) == k:
                ans = max(ans, s)
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]
            s -= out
        return ans
