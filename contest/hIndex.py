from typing import List
from bisect import bisect_left

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations == [0]:
            return 0
        for i in citations:
            ind = bisect_left(citations,i)
            if (len(citations) - ind) == i:
                return i