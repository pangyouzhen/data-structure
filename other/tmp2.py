
from typing import List


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        ans = 0
        restricted = set(restricted)
        print(g)
        def dfs(start: int, fa: int):
            nonlocal ans
            ans += 1
            for next in g[start]:
                if next != fa and next not in restricted:
                    dfs(next, start)
        dfs(0, -1)
        return ans


if __name__ == "__main__":
    n = 7
    edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
    restricted = [4, 2, 1]
    # n = 4
    # edges = [[2, 1], [1, 0], [0, 3]]
    # restricted = [3, 2]
    func = Solution().reachableNodes
    print(func(n, edges, restricted))
