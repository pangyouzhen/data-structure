import bisect
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.sort(key=lambda v: abs(v -x))
        return sorted(arr[:k])
        


if __name__ == "__main__":
    arr = [
        1,
    ]
    k = 1
    x = 1
    func = Solution().findClosestElements
    print(func(arr, k, x))
