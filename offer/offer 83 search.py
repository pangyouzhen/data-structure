from typing import List
from collections import Counter


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return Counter(nums)[target]


if __name__ == '__main__':
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(sol.search(nums, target))
