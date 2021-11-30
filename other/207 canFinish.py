from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #  dfs 没法判断有环还是没有环，需要对visited进行改造
        def dfs(graph, start, visited=None):
            if visited is None:
                visited = set()
            visited.add(start)
            for next_ in graph[start] - visited:
                dfs(graph, next_, visited)
            return visited

        def dfs2(i, adjacency, flags):
            if flags[i] == -1: return True
            if flags[i] == 1: return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs2(j, adjacency, flags): return False
            flags[i] = -1
            return True

        adjacency = [[] for _ in range(numCourses)]
        flags = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs2(i, adjacency, flags): return False
        return True



if __name__ == '__main__':
    numCourses = 2
    prerequisites = [[1, 0]]
    sol = Solution()
    print(sol.canFinish(numCourses, prerequisites))
