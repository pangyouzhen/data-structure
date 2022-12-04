from typing import List
from math import inf


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, d in roads:
            g[x - 1].append((y - 1, d))
            # 双向图，所以每个都对应的 x,y都会增加
            g[y - 1].append((x - 1, d))
        print(g)
        ans = inf
        vis = [False] * n

        def dfs(x: int) -> None:
            nonlocal ans
            vis[x] = True
            for y, d in g[x]:
                ans = min(ans, d)
                if not vis[y]:
                    dfs(y)

        dfs(0)
        return ans


if __name__ == "__main__":
    func = Solution().minScore
    n = 4
    roads = [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]
    print(func(n, roads))
