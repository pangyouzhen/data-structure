from typing import List
from collections import Counter


class Solution:
    def divideArray(self, nums: List) -> bool:
        c = Counter(nums)
        for k, v in c.items():
            if v % 2 != 0:
                return False
        return True


if __name__ == "__main__":
    func = Solution().divideArray
    nums = []
    print(func(nums))
