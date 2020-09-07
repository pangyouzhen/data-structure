from collections import Counter
from typing import List


# nlog(n) 的复杂度
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t = Counter(nums)
        keyvalues = sorted(t.items(), key=lambda x: (x[1], x[0]), reverse=True)
        return [i[0] for i in keyvalues[:k]]


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    sol = Solution()
    print(sol.topKFrequent(nums, 2))
