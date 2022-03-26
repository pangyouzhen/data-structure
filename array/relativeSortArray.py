from typing import Counter, List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c1 = Counter(arr1)
        not_exits = []
        res = []
        for k in arr2:
            v1 = c1[k]
            for i in range(v1):
                res.append(k)
        diff_keys = c1.keys() - Counter(arr2).keys()
        for diff_key in diff_keys:
            tmp = c1[diff_key]
            for j in range(tmp):
                not_exits.append(diff_key)
        not_exits.sort()
        res.extend(not_exits)
        return res
                
                
if __name__ == "__main__":
    sol = Solution()
    func = sol.relativeSortArray
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    print(func(arr1,arr2))