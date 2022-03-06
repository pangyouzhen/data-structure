from typing import List
from collections import defaultdict


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        last = None
        d = defaultdict(int)
        for i in nums:
            if last == key:
                d[i] += 1
            last = i
        max_val = float("-inf")
        max_key = None
        for k, v in d.items():
            if v > max_val:
                max_key = k
                max_val = v
        return max_key


if __name__ == '__main__':
    nums = [2, 2, 2, 2, 3]
    key = 2
    func = Solution().mostFrequent
    print(func(nums, key))
