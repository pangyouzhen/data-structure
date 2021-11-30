from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def combinationSum(self, candidates: List[int], target: int):
        one_ans = []
        start = 0
        candidates.sort()
        self.combination_sum_memo(candidates, target, start, one_ans)
        return self.res

    def combination_sum_memo(self, candidates: List[int], target: int, start: int, one_ans: List[int]):
        if target == 0:
            self.res.append(one_ans[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            one_ans.append(candidates[i])
            self.combination_sum_memo(candidates, target - candidates[i], i, one_ans)
            one_ans.pop()
        return


if __name__ == '__main__':
    sol2 = Solution()
    print(sol2.combinationSum([2, 3, 6, 7], 7))
    print(sol2.combinationSum([2, 3, 5], 8))
    print(sol2.combinationSum([8, 7, 4, 3], 11))
