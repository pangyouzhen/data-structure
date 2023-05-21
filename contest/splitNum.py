from collections import Counter


class Solution:
    def splitNum(self, num: int) -> int:
        s = str(num)
        # 交替找数字
        s = sorted(s)
        l = len(s)
        nums1 = [s[i] for i in range(0, l, 2)]
        nums2 = [s[i] for i in range(1, l, 2)]
        n1 = int("".join(nums1))
        n2 = int("".join(nums2))
        return n1 + n2
