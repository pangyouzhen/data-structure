from typing import List, Dict, Tuple
from collections import defaultdict


class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        g = defaultdict(set)
        for x, y in edges:
            g[x].add(y)
            g[y].add(x)
        # 这里要用set，不然性能过不去
        self.restricted = set(restricted)
        self.ans = 0
        visited = set()
        self.dfs(g, 0, visited)
        return self.ans

    def dfs(self, g: Dict[int, Tuple], start: int, visited: Tuple):
        visited.add(start)
        # print(start)
        self.ans += 1
        for next in g[start]:
            if next not in self.restricted and next not in visited:
                self.dfs(g, next, visited)


if __name__ == "__main__":
    n = 7
    edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
    restricted = [4, 2, 1]
    # n = 4
    # edges = [[2, 1], [1, 0], [0, 3]]
    # restricted = [3, 2]
    func = Solution().reachableNodes
    print(func(n, edges, restricted))
