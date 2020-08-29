from typing import List
from functools import reduce


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        temp = arr[1] - arr[0]
        for i, v in enumerate(arr[1:]):
            val = arr[i + 1] - arr[i]
            if val != temp:
                return False
        return True
