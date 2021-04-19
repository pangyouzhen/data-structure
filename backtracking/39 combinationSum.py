from typing import List


class Solution:
    def combinationSum(self, candidates, target: int):
        global res
        res = []
        one_ans = []

        def combinationSum_memo(candidates, target, start, one_ans):
            if target == 0:
                res.append(one_ans[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target: return
                one_ans.append(candidates[i])
                combinationSum_memo(candidates, target - candidates[i], i, one_ans)
                one_ans.pop()
            return

        start = 0
        candidates.sort()
        combinationSum_memo(candidates, target, start, one_ans)
        return res


if __name__ == '__main__':
    sol2 = Solution()
    print(sol2.combinationSum([2, 3, 6, 7], 7))
    print(sol2.combinationSum([2, 3, 5], 8))
    print(sol2.combinationSum([8, 7, 4, 3], 11))
