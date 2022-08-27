from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for i in arr2:
            if i in arr1:
                res.extend([i] * arr1.count(i))
        not_exists = sorted(list(set(arr1) - set(arr2)))
        for i in not_exists:
            res.extend([i] * arr1.count(i))
        return res


if __name__ == "__main__":
    sol = Solution()
    func = sol.relativeSortArray
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    print(func(arr1, arr2))
