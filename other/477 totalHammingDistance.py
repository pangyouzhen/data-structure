from itertools import combinations
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for j in combinations(nums, 2):
            print(j)
            res += bin(j[0] ^ j[1]).count("1")
        return res


if __name__ == '__main__':
    a = [4, 12, 2]
    sol = Solution()
    print(sol.totalHammingDistance(a))
