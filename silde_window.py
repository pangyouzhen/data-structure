from typing import List
from collections import deque


class Solution:
    def slide_window(self, arr: List[int], k) -> int:
        q = [None] * k
        # python 实现固定长度队列，增加一个就删除一个
        t = 0
        result = []
        while t < len(arr):
            q.append(arr[t])
            del q[0]
            if None not in q:
                result.append(max(q))
            t += 1
        return max(result)


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(sol.slide_window(nums, k))

# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# ————————————————
