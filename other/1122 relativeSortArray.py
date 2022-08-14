from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for i in arr2:
            if i in arr1:
                c = arr1.count(i)
                res.extend([i] * c)
        other = []
        for i in arr1:
            if i in res:
                pass
            else:
                other.append(i)
        other.sort()
        res.extend(other)
        return res

if __name__ == '__main__':
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    sol = Solution()
    print(sol.relativeSortArray(arr1,arr2))
