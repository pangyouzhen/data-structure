# graph = {'A': set(['B', 'C']),
#          'B': set(['A', 'D', 'E']),
#          'C': set(['A', 'F']),
#          'D': set(['B']),
#          'E': set(['B', 'F']),
#          'F': set(['C', 'E'])}
#

#
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


# graph = {'A': set(['B', 'C']),
#          'B': set(['A', 'D', 'E']),
#          'C': set(['A', 'F']),
#          'D': set(['B']),
#          'E': set(['B', 'F']),
#          'F': set(['C', 'E'])}


# dfs  three element : graph,start,visited
#  递归的方式，更好理解
#  
def dfs2(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs2(graph, next, visited)
    #      递归的方式，for循环里面进行遍历就OK了
    return visited


from collections import deque


# bfs 分为两部分，因为不需要递归，所以输入graph 和 root就OK
# 1. visited: set  部分
# 2. not visited: heap_queue
#  while heap_queue：
#       移除quue头部元素，放在visited中
#       根据头部元素，广度优先，找到相近的节点
#       把相近节点放入visited中，同时为了遍历下一层，放在 queue中

def bfs(graph, root):
    visited, queue = set(), deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        for neightbour in graph[vertex]:
            if neightbour not in visited:
                visited.add(neightbour)
                queue.append(neightbour)
    return visited


if __name__ == '__main__':
    #  无向图，所以每个节点，都有对应的值
    #  图的两种表现方式
    graph2 = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [1], 4: [2]}
    #  这里的dfs 和 bfs 两个是对应不同的 结构的 graph1 = {"a":set(1,1)},graph2 = {"a":[1]}
    print(dfs(graph2, 0))
    print(bfs(graph2, 0))
    # print(dfs2(graph, "A"))
