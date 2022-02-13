from bisect import bisect


from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.lst = nums 
        self.target = k
        self.lst.sort()

    def add(self, val: int) -> int:
        bisect.insort(self.lst,val)
        return self.lst[-self.target]