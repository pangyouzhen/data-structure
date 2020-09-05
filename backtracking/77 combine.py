from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        all_ans = []
        one_ans = []

        def dfs(all_ans, one_ans, array):
            if len(one_ans) == k:
                all_ans.append(one_ans[:])
                return
            for i in range(len(array)):
                one_ans.append(array[i])
                dfs(all_ans, one_ans, array[i + 1:])
                one_ans.pop()

        dfs(all_ans, one_ans, list(range(1, n + 1)))
        return all_ans


    def combine_(self, nums: List[int], k: int) -> List[List[int]]:
        all_ans = []
        one_ans = []

        def dfs(all_ans, one_ans, array):
            if len(one_ans) == k:
                all_ans.append(one_ans[:])
                return
            for i in range(len(array)):
                one_ans.append(array[i])
                dfs(all_ans, one_ans, array[i + 1:])
                one_ans.pop()

        dfs(all_ans, one_ans, list(range(1, n + 1)))
        return all_ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.combine(4, 2))
