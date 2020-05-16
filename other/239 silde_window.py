from typing import List
from collections import deque
from array import array
import timeit
from random import randint
from overrides import overrides


# Monotonic Queue 单调队列
# class MonotonicQueue(deque):
#     def __init__(self, iterable, max_len):
#         deque.__init__(self, iterable, max_len)
#
#     # @overrides
#     def append(self, x: _T) -> None:
#         for i in self.__iter__():
#             if x > i:
#                 self.remove(i)


def timer(function):
    def new_function(*args, **kwargs):
        start_time = timeit.default_timer()
        result = function(*args, **kwargs)
        elapsed = timeit.default_timer() - start_time
        print('Function "{name}" took {time} seconds to complete.'.format(name=function.__name__, time=elapsed))
        # return result

    return new_function


#  TimeOut
# class Solution4:
#     @timer
#     def maxSlidingWindow(self, arr: List[int], k) -> List[int]:
#         q = [None] * k
#         # python 实现固定长度队列，增加一个就删除一个
#         t = 0
#         result = []
#         while t < len(arr):
#             q.append(arr[t])
#             del q[0]
#             if None not in q:
#                 result.append(max(q))
#             t += 1
#         return result


class Solution5:
    @timer
    def maxSlidingWindow(self, arr: List[int], k) -> List[int]:
        q = arr[:k - 1]
        # python 实现固定长度队列，增加一个就删除一个
        result = []
        for i in arr[k - 1:]:
            q.append(i)
            del q[0]
            result.append(max(q))
        return result


class Solution:
    @timer
    def maxSlidingWindow(self, arr: List[int], k) -> List[int]:
        q = deque(maxlen=k)
        # python 实现固定长度队列，增加一个就删除一个
        t = 0
        result = []
        while t < len(arr):
            q.append(arr[t])
            result.append(max(q))
            t += 1
        return result[k - 1:]


# 递增队列
class Solution2:
    @timer
    def maxSlidingWindow(self, arr: List[int], k) -> List[int]:
        q = deque(arr[:k - 1], maxlen=k)
        # python 实现固定长度队列，增加一个就删除一个
        result = []
        temp = []
        for i, v in enumerate(arr[k - 1:]):
            temp.append(v)
            for inx, val in enumerate(temp):
                if val < v:
                    temp.pop(inx)
            result.append(temp[0])
        return result


class Solution3:
    @timer
    def maxSlidingWindow(self, arr: List[int], k) -> List[int]:
        arr = array('i', arr)
        q = deque(arr[:k - 1], maxlen=k)
        # python 实现固定长度队列，增加一个就删除一个
        t = 0
        result = []
        for i in arr[k - 1:]:
            q.append(i)
            result.append(max(q))
            t += 1
        return result


# class Solution:
#     def maxSlidingWindow(self, arr: List[int], k) -> List[int]:
#         q = [None] * k
#         # python 实现固定长度队列，增加一个就删除一个
#         t = 0
#         result = []
#         while t < len(arr):
#             q.append(arr[t])
#             del q[0]
#             if None not in q:
#                 result.append(max(q))
#             t += 1
#         return result
class Solution6:
    @timer
    def maxSlidingWindow(self, arr, k):
        que = [(-1000000, 1000000)]
        ans = []
        for i in range(len(arr)):
            print(f'{que}---------{i}----{arr[i]}')
            while len(que) > 0 and i - que[0][0] >= k:
                del que[0]
            while len(que) > 0 and que[-1][1] <= arr[i]:
                que.pop()
            que.append((i, arr[i]))
            if i >= k - 1:
                ans.append(que[0][1])
        return ans


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    # nums = []
    # for i in range(1000000):
    #     nums.append(randint(1, 10000000))
    # k = 5000
    # sol = Solution()
    # print(sol.maxSlidingWindow(nums, k))
    #
    sol = Solution2()
    print(sol.maxSlidingWindow(nums, k))

    # sol = Solution3()
    # print(sol.maxSlidingWindow(nums, k))
    #
    # sol = Solution4()
    # print(sol.maxSlidingWindow(nums, k))
    #
    # sol = Solution5()
    # print(sol.maxSlidingWindow(nums, k))
    # res = sol.maxSlidingWindow(nums, k)
    # assert res == [3, 3, 5, 5, 6, 7]

    sol = Solution6()
    print(sol.maxSlidingWindow(nums, k))

# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1] 3  -1 -3  5  3  6  7        1  [1]
# [1  3]  -1  -3  5  3  6  7       3 [3]
# [1  3  -1] -3  5  3  6  7       3   [3,-1]
#  1 [3  -1  -3] 5  3  6  7       3   [3,-1,-3]
#  1  3 [-1  -3  5] 3  6  7       5  [5]
#  1  3  -1 [-3  5  3] 6  7       5  [5,3]
#  1  3  -1  -3 [5  3  6] 7       6   [6]
#  1  3  -1  -3  5 [3  6  7]      7   [7]
# ————————————————
