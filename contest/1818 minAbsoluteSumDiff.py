from typing import List
import bisect


class Solution:
    #  贪心替换是错误的，比如下面的例子
    # nums1 = [1, 28, 21]
    # nums2 = [9, 21, 20]
    def minAbsoluteSumDiff(self, nums1, nums2) -> int:
        n, total, sl, ans = len(nums1), 0, sorted(nums1), float("inf")
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            total += diff
            idx = bisect.bisect_left(sl, nums2[i])
            # idx > 0 尝试用idx-1替换当前值
            if idx:
                ans = min(ans, abs(sl[idx - 1] - nums2[i]) - diff)
            # idx < n 尝试用idx替换当前值
            if idx < n:
                ans = min(ans, abs(sl[idx] - nums2[i]) - diff)
        return (total + ans) % (10 ** 9 + 7) if total else total


if __name__ == '__main__':
    nums1 = [1, 10, 4, 4, 2, 7]
    nums2 = [9, 3, 5, 1, 7, 4]

    sol = Solution()

    # print(sol.get_nums_max_index(nums1, nums2))
    print(sol.minAbsoluteSumDiff(nums1, nums2))
