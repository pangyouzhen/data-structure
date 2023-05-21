import itertools
from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        if k == 1:
            return min(nums)
        l = len(nums)
        for i in itertools.combinations(nums,k):
            print(i)


if __name__ == "__main__":
    sol = Solution().minCapability
    nums = [2,3,5,9]
    k = 2
    print(sol(nums,k))