from typing import List
import heapq


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        return heapq.nsmallest(k, arr)


if __name__ == '__main__':
    arr = [3, 2, 1]
    k = 2
    sol = Solution()
    print(sol.getLeastNumbers(arr, k))
