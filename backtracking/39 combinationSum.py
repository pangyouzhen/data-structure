from typing import List


class Solution(object):
    def combinationSum(self, candidates, target):
        def dfs(candidates, target, s, one_ans, all_ans):
            if target == 0:
                all_ans.append(one_ans[:])
                return

            for i in range(s, len(candidates)):
                if candidates[i] > target: return
                one_ans.append(candidates[i])
                dfs(candidates, target - candidates[i], i, one_ans, all_ans)
                one_ans.pop()

        ans = []
        candidates.sort()
        dfs(candidates, target, 0, [], ans)

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))
