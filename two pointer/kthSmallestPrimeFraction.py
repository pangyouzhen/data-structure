import fractions
import itertools
from typing import List
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        vals = itertools.combinations(arr, 2)
        t = []
        v = [fractions.Fraction(i, v) for i, v in vals]
        v.sort()
        t = v[k-1]
        return [t.numerator, t.denominator]
    
if __name__ == "__main__":
    func = Solution().kthSmallestPrimeFraction
    arr = [1,2,3,5]
    k = 3
    print(func(arr,k))