from typing import List


class Solution:
    # TODO
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        # 就是找到一个小于sessionTime的最大值
        k = 0
        while True:
            k += 1

    def tw_pointer(self, l: List[int], sesstionTime):
        left = 0
        right = len(l) - 1
        val = 0
        ind = []
        while left < right and val < sesstionTime:
            if l[right] == sesstionTime:
                ind.append(right)
                break
            elif (l[right] + l[left]) == sesstionTime:
                ind.append(left)
                ind.append(right)
                break
            elif (l[right] + l[left]) < sesstionTime:
                ind.append(left)
                ind.append(right)
                val = l[right] + l[left]
