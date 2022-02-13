from typing import List
from collections import Counter
import heapq


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd = []
        even = []
        for i, v in enumerate(nums):
            if i % 2 == 0:
                even.append(v)
            else:
                odd.append(v)
        c_odd = Counter(odd)
        c_even = Counter(even)

        h_odd = heapq.heappush(c_odd)
        h_even = heapq.heappush(c_even)



if __name__ == '__main__':
    sol = Solution()
    func = sol.minimumOperations
