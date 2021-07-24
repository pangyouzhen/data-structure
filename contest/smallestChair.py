from typing import List
import pysnooper


class Solution:
    @pysnooper.snoop()
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target = times[targetFriend][0]
        # print(target)
        in_queue = [0] * len(times)
        times_dic = {time[0]: time[1] for time in times}
        all_value = list(set([i[0] for i in times] + [i[1] for i in times]))
        all_value.sort()
        v = times_dic.values()
        k = times_dic.keys()
        for t in all_value:
            if t in v:
                ind = in_queue.index(t)
                in_queue[ind] = 0
            if t in k:
                ind = in_queue.index(0)
                in_queue[ind] = times_dic[t]
                if t == target:
                    return ind


if __name__ == '__main__':
    # times = [[3, 10], [1, 5], [2, 6]]
    # times = [[5, 10], [1, 4], [2, 3]]
    # targetFriend = 0
    # times = [[3, 10], [1, 5], [2, 6]]
    # targetFriend = 0
    times = [[1, 4], [2, 3], [4, 6]]
    targetFriend = 1
    # times = [[33889, 98676], [80071, 89737], [44118, 52565], [52992, 84310], [78492, 88209], [21695, 67063],
    #          [84622, 95452],
    #          [98048, 98856], [98411, 99433], [55333, 56548], [65375, 88566], [55011, 62821], [48548, 48656],
    #          [87396, 94825],
    #          [55273, 81868], [75629, 91467]]
    # targetFriend = 6
    # times = [[4, 5], [12, 13], [5, 6], [1, 2], [8, 9], [9, 10], [6, 7], [3, 4], [7, 8], [13, 14], [15, 16], [14, 15],
    #          [10, 11],
    #          [11, 12], [2, 3], [16, 17]]
    # targetFriend = 15
    sol = Solution()
    print(sol.smallestChair(times, targetFriend))
