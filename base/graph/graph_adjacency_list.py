from typing import Dict, Set, Tuple,List


graph: Dict[str, Set[str]] = {'A': {'B', 'C'},
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


def dfs(graph: Dict[str, Tuple[int]], start: str, all_res: List[str]):
    visited.add(start)
    all_res.append(start)
    for next in graph[start]:
        if next not in visited:
            dfs(graph, next, all_res)


if __name__ == '__main__':
    visited = set()
    all_res = []
    dfs(graph3, "0", all_res)
    print(all_res)
