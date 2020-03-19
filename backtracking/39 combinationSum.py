from typing import List


class Solution(object):
    def combinationSum(self, candidates, target):
        def dfs(candidates, target, s, curr, ans):
            if target == 0:
                ans.append(curr[:])
                return

            for i in range(s, len(candidates)):
                if candidates[i] > target: return
                curr.append(candidates[i])
                dfs(candidates, target - candidates[i], i, curr, ans)
                curr.pop()

        ans = []
        candidates.sort()
        dfs(candidates, target, 0, [], ans)

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum([2, 3, 6, 7], 7))
