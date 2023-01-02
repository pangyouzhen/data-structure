from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.all_ans = []
        one_ans = [0]
        self.dfs(0, one_ans)
        return self.all_ans

    def dfs(self, k, one_ans):
        if k == len(graph) - 1:
            # if one_ans[-1] == len(self.graph) -1:
            self.all_ans.append(one_ans[:])
            return
        for i in self.graph[k]:
            one_ans.append(i)
            self.dfs(i, one_ans)
            one_ans.pop()


if __name__ == "__main__":
    func = Solution().allPathsSourceTarget
    # graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    # graph = [[4,3,1],[3,2,4],[],[4],[]]
    graph = [[2], [], [1]]
    print(func(graph))
