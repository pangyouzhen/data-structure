from collections import Counter
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c = Counter(nums)
        curr = 1
        n = c[1]
        # 偶数要取到奇数
        if n % 2 ==0:
            curr = max((n/2) - 1,curr)
        else:
            curr = n
        del c[1]
        for i in c:
            res = 0
            while True:
                if i not in c:
                    # 思路对了,写起来错了
                    res -= 1
                    break
                if c[i] % 2== 1:
                    res += 1
                    break
                res += 2
                i *= i
            curr = max(res, curr)
        return curr


# nums0 = [5, 4, 1, 2, 2]
# nums1 = [1, 3, 2, 4]
# nums2 = [1, 3, 2, 4, 9, 3, 3]
nums3 = [1, 1, 1]
func = Solution().maximumLength
# print(func(nums0))
# print(func(nums1))
# print(func(nums2))
print(func(nums3))
