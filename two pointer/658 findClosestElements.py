import bisect
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = len(arr)
        if k >= l:
            return arr
        l = bisect.bisect_left(arr,x)
        r = bisect.bisect_right(arr,x)
        if k <= (r - l):
            return arr[l:l + k]
        if r == l:
            return arr[-k:]
        res = arr[l:r]
        k -= r - l
        while k > 0:
            if abs(x - arr[l - 1]) <= abs(x - arr[r]):
                res.append(arr[l - 1])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            k -= 1
        res.sort()
        return res


if __name__ == "__main__":
    arr = [
        1,
    ]
    k = 1
    x = 1
    func = Solution().findClosestElements
    print(func(arr, k, x))
