from typing import List
from bisect import bisect


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        mat_array = np.array(mat)
        mat_array.sort(axis=1)
        a = mat_array.sum(axis=0)
        if target in a:
            return 0
        elif target > a[-1]:
            return abs(a[-1] - target)
        elif target < a[0]:
            return abs(a[0] - target)
        else:
            ind = bisect(a, target)
            subtract_value = target - a[ind - 1]
            v = mat_array[:, ind] - mat_array[:, ind - 1]
            v.sort()
            if subtract_value in v:
                return 0
            t = np.cumsum(v)
            ind = bisect(t, subtract_value)
            return min(abs(subtract_value - t[ind]), abs(subtract_value - t))


if __name__ == '__main__':
    # mat = [[1], [2], [3]]
    # target = 100
    mat = [[1, 2, 9, 8, 7]]
    target = 6
    func = Solution().minimizeTheDifference
    print(func(mat, target))
