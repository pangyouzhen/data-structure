from bisect import insort, bisect
from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapper = {str(i): str(v) for i, v in enumerate(mapping)}
        vals = []
        res = []
        for i in nums:
            s_number = str(i)
            val = ""
            for j in s_number:
                val += mapper[j]
            val_int = int(val)
            ind = bisect(vals, val_int)
            insort(vals, val_int)
            res.insert(ind, i)
        return res


if __name__ == '__main__':
    func = Solution().sortJumbled
    mapping = [8, 9, 4, 0, 2, 1, 3, 5, 7, 6]
    nums = [991, 338, 38]
    print(func(mapping, nums))
