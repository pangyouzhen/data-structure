from typing import List
from itertools import combinations


class Solution:
    def __init__(self):
        self.all_ans = []

    def countQuadruplets(self, nums: List[int]) -> int:
        one_ans = []
        self.countQuadruplets_memo(nums, 0, one_ans)
        res = 0
        for j in self.all_ans:
            if sum(j[:3]) == j[-1]:
                res += 1
        print(f"all ans", self.all_ans)
        return res

    def countQuadruplets_memo(self, nums: List[int], start: int, one_ans: List[int]) -> None:
        if len(one_ans) == 4:
            self.all_ans.append(one_ans[:])
            print("---------------")
            return
        for i in range(start, len(nums)):
            print(f"for i in range({start}:{len(nums)})")
            one_ans.append(nums[i])
            self.countQuadruplets_memo(nums, i + 1, one_ans)
            one_ans.pop()

    def countQuadruplets2(self, nums: List[int]) -> int:
        res = 0
        for i in combinations(nums, 4):
            i_ls = list(i)
            if sum(i_ls[:3]) == i_ls[-1]:
                res += 1
        return res


if __name__ == '__main__':
    func = Solution().countQuadruplets2
    nums = [1, 1, 1, 3, 5]
    print(func(nums))
