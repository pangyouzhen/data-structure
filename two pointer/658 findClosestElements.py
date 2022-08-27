from bisect import bisect
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ind = bisect(arr, x)
        res = []
        left = ind - 1
        right = ind
        while len(res) <= k:
            if left < 0:
                res.extend(arr[right:right + k - len(res)])
                res.sort()
                return res
            if right >= len(arr):
                res.extend(arr[left + len(res) - k: left])
                res.sort()
                return res
            if abs(arr[left] - x) < abs(arr[right] - x):
                res.append(arr[left])
                left -= 1
            elif abs(arr[left] - x) > abs(arr[right] - x):
                res.append(arr[right])
                right += 1
            else:
                res.append(arr[left])
                res.append(arr[right])
                left -= 1
                right += 1
        res.sort()
        return res[:k]


if __name__ == '__main__':
    arr = [1, ]
    k = 1
    x = 1
    func = Solution().findClosestElements
    print(func(arr, k, x))
