from collections import Counter, defaultdict
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        a = defaultdict(list)
        for i, v in c.items():
            a[v].append(i)
        k = sorted(a.keys())
        res = []
        for i in k:
            for j in sorted(a[i], reverse=True):
                res.extend([j] * i)
        return res


if __name__ == '__main__':
    func = Solution().frequencySort
    nums = [1, 1, 2, 2, 2, 3]
    print(func(nums))
