from collections import Counter
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        c = Counter(nums)
        ks = list(c.keys())
        ks.sort()
        res = 1
        for i in ks:
            curr = 1
            if i == 1:
                n = c[i]
                if n % 2 == 0:
                    curr = (n / 2) - 1
                else:
                    curr = n
                    continue
            two_ = 1
            # 必须对称的2个元素
            if c[i] % 2 != 0:
                continue
            while two_:
                v = i ** two_
                # 如果在这里面
                if v in ks:
                    # 只有1个时候
                    if c[v] == 1:
                        break
                    # 如果>=2个
                    else:
                        # 也有可能+2, 也可能+1
                        # +2 是 下一个元素有，
                        # +1 是：下一个元素没有
                        # 深度优先算法，直到没有的时候终止
                        two_ += 1
                        t = i ** two_
                        if t in ks:
                            curr += 2
                        else:
                            curr += 1
            res = max(res, curr)
        return res


# nums0 = [5, 4, 1, 2, 2]
# nums1 = [1, 3, 2, 4]
# nums2 = [1, 3, 2, 4, 9, 3, 3]
nums3 = [1, 1, 1]
func = Solution().maximumLength
# print(func(nums0))
# print(func(nums1))
# print(func(nums2))
print(func(nums3))
