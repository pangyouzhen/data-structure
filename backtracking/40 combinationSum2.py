from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        start = 0
        one_ans = []
        candidates.sort()
        self.combination_sum_memo(candidates, target, start, one_ans)
        return self.res

    def combination_sum_memo(self, candidates: List[int], target: int, start: int, one_ans: List[int]):
        if target < 0:
            return
        if target == 0:
            if one_ans not in self.res:
                self.res.append(one_ans[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            one_ans.append(candidates[i])
            self.combination_sum_memo(candidates, target - candidates[i], i + 1, one_ans)
            one_ans.pop()
        return


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum2([2, 5, 1, 2, 2], 5))
