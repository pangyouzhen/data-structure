from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        global res
        res = []
        start = 0
        one_ans = []
        candidates.sort()
        print(candidates)
        self.combinationSum2_memo(candidates, target, start, one_ans)
        return res

    def combinationSum2_memo(self, candidates, target, start, one_ans):
        if target < 0:
            return
        if target == 0:
            if one_ans not in res:
                res.append(one_ans[:])
            print("--------------")
            return
        for i in range(start, len(candidates)):
            print(f'{(start + 1) * "+"},for {i=} in range({start=},{len(candidates)=}), {target = },{one_ans = }')
            if candidates[i] > target:
                return
            one_ans.append(candidates[i])
            self.combinationSum2_memo(candidates, target - candidates[i], i + 1, one_ans)
            one_ans.pop()
        return


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum2([2, 5, 1, 2, 2], 5))
