from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        all_ans = []
        one_ans = []

        def dfs(target, one_ans, all_ans, array):
            if target == 0 and one_ans not in all_ans :
                all_ans.append(one_ans[:])
                return
            elif target < 0:
                return
            for i in range(len(array)):
                one_ans.append(array[i])
                dfs(target - array[i], one_ans, all_ans, array[i + 1:])
                one_ans.pop()

        candidates.sort()
        dfs(target, one_ans, all_ans, candidates)
        return all_ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum2([2, 5, 1, 2, 2], 5))
