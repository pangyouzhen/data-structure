from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(target, one_ans, all_ans, array):
            if target == 0 and len(one_ans) == k:
                all_ans.append(one_ans[:])
                return
            elif target < 0:
                return
            for i in range(len(array)):
                if array[i] > target: break
                one_ans.append(array[i])
                dfs(target - array[i], one_ans, all_ans, array[i + 1:])
                one_ans.pop()

        one_ans = []
        all_ans = []
        dfs(n, one_ans, all_ans, list(range(1, 10)))
        return all_ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.combinationSum3(3, 15))
