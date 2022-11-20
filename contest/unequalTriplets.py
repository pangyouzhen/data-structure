from typing import List
from itertools import permutations,combinations


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return 0
        res = 0
        for i in combinations(nums, 3):
            if len(i) == len(set(i)):
               res += 1
        return res 


if __name__ == "__main__":
    func = Solution().unequalTriplets
    num = [4, 4, 2, 4, 3]
    print(func(num))
