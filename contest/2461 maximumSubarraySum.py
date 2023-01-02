from collections import Counter
from typing import List


class Solution:
    # 时间复杂度的问题
    # list 切片的时间复杂度为k，所以整体时间复杂度为O(kn)
    # 通过k和n的范围算出时间会远远超出
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
        # 用滑动窗口的核心问题是初始如果是重复的怎么算的
        # 这里用dict的长度来判断是否含有重复元素
        ans = 0
        cnt = Counter(nums[:k - 1])
        s = sum(nums[:k - 1])
        for in_, out in zip(nums[k - 1:], nums):
            print(in_,out)
            cnt[in_] += 1
            s += in_
            if len(cnt) == k:
                ans = max(ans, s)
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]
            s -= out
        return ans

if __name__ == "__main__":
    func = Solution().maximumSubarraySum
    nums=[4,4,4,5,6]
    k = 3
    print(func(nums,k))