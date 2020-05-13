graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


# dfs  three element : graph,start,visited
def dfs2(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


from collections import deque


def bfs(graph, root):
    visited, queue = set(), deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        for neightbour in graph[vertex]:
            if neightbour not in visited:
                visited.add(neightbour)
                queue.append(neightbour)


if __name__ == '__main__':
    print(dfs(graph, "A"))
    print(bfs(graph, 'A'))
    print(dfs2(graph,"A"))
