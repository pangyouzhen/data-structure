from typing import Dict
from typing import List

from pysnooper import snoop

graph: Dict[str, set[str]] = {'A': {'B', 'C'},
                              'B': {'A', 'D', 'E'},
                              'C': {'A', 'F'},
                              'D': {'B'},
                              'E': {'B', 'F'},
                              'F': {'C', 'E'}}

graph2: Dict[str, List[str]] = {'A': ['B', 'C'],
                                'B': ['A', 'D', 'E'],
                                'C': ['A', 'F'],
                                'D': ['B'],
                                'E': ['B', 'F'],
                                'F': ['C', 'E']}

graph3 = {'0': {'1', '2'},
          '1': {'0', '3', '4'},
          '2': {'0'},
          '3': {'1'},
          '4': {'2', '3'}}


@snoop()
def dfs(graph: Dict[str, set[str]], start: str, visited=None):
    #  todo 为什么有时不是从start 出发的？程序有问题？
    #  todo 这个程序对有向图和无向图均适用？
    if visited is None:
        visited = set()
    visited.add(start)
    # print(start)
    for next in (graph[start] - visited):
        dfs(graph, next, visited)
    return visited


if __name__ == '__main__':
    print(dfs(graph3, "0"))
