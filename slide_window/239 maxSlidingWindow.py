import timeit
from array import array
from collections import deque
from typing import List


# int left = 0, right = 0;
#
# while (right < s.size()) {
#     // 增大窗口
#     window.add(s[right]);
#     right++;
#
#     while (window needs shrink) {
#         // 缩小窗口
#         window.remove(s[left]);
#         left++;
#     }
# }


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def mon_arr(arr):
            n = len(arr)
            # TODO 这不是单调队列
            while n > 1 and arr[0] < arr[-1]:
                arr.pop(0)

        fst_val = nums[0:k]
        max_val = max(fst_val)
        fst_val = fst_val[fst_val.index(max_val):]
        res = [max_val]
        for i in range(k, len(nums)):
            print(fst_val)
            fst_val.append(nums[i])
            if len(fst_val) > k:
                fst_val.pop(0)
            mon_arr(fst_val)
            res.append(fst_val[0])
        return res


if __name__ == '__main__':
    # nums = [1, 3, -1, -3, 5, 3, 6, 7]
    # k = 3
    sol = Solution()
    # print(sol.maxSlidingWindow(nums, k))
    nums2 = [1, 3, 1, 2, 0, 5]
    print(sol.maxSlidingWindow(nums2, k=3))

# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3   [3,-1]
#  1 [3  -1  -3] 5  3  6  7       3   [3,-1,-3]
#  1  3 [-1  -3  5] 3  6  7       5  [5]
#  1  3  -1 [-3  5  3] 6  7       5  [5,3]
#  1  3  -1  -3 [5  3  6] 7       6   [6]
#  1  3  -1  -3  5 [3  6  7]      7   [7]
# ————————————————
