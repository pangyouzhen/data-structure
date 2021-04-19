from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        global res
        res = []
        start = 0
        one_ans = []
        candidates.sort()

        def combinationSum2_memo(candidates, target, start, one_ans):
            if target < 0:
                return
            if target == 0:
                if one_ans not in res:
                    res.append(one_ans[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    return
                one_ans.append(candidates[i])
                combinationSum2_memo(candidates, target - candidates[i], i + 1, one_ans)
                one_ans.pop()
            return

        combinationSum2_memo(candidates, target, start, one_ans)
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum2([2, 5, 1, 2, 2], 5))
