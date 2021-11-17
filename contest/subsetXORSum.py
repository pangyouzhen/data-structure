from itertools import product, combinations
from functools import reduce


class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = sum(nums)
        for i in range(2, len(nums) + 1):
            for j in (combinations(nums, i)):
                res += reduce(lambda x, y: x ^ y, j)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsetXORSum([3, 4, 5, 6, 7, 8]))
