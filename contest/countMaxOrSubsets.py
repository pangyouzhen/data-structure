from typing import List
from functools import reduce
from collections import Counter


class Solution:
    def __init__(self):
        self.res: List[List[int]] = []

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # nums.sort()
        def or_result(x, y):
            return x | y

        self.res = self.subsets(nums)
        _ = [reduce(or_result, i) for i in self.res if i]
        c = Counter(_)
        key = max(c.keys())
        return c[key]

    def subsets(self, nums):
        one_ans = []
        start = 0
        self.nums_len = len(nums)
        self.subsets_memo(nums, start, one_ans)
        return self.res

    def subsets_memo(self, nums, start, one_ans):
        # 纵向，因为是取所有的子集，所以这里的没有终止条件
        self.res.append(one_ans[:])
        nums_len = len(nums)
        for i in range(start, nums_len):
            one_ans.append(nums[i])
            self.subsets_memo(nums, i + 1, one_ans)
            one_ans.pop()
        return


if __name__ == '__main__':
    nums = [3, 2, 1, 5]
    func = Solution().countMaxOrSubsets
    print(func(nums))
