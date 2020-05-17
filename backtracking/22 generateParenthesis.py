# https://www.bilibili.com/video/av45844036?from=search&seid=4933796386934297862
from typing import Dict, List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        #  深度优先算法 -> 回溯法
        def dfs(graph:
        Dict, start: str, visited=None):
            #  深度优先算法的核心也是递归
            if visited == None:
                visited = set()
            visited.add(start)
            for next_ in graph[start] - visited:
                dfs(graph, next_, visited)
            return visited

        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(4))
    print(sol.generateParenthesis(6))
