from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def set_keys_station(self):
        keyStation = {}
        key = list(self.graph.keys())
        if len(key) < self.V:
            for i in key:
                for j in self.graph[i]:
                    if j not in key:
                        key.append(j)
        for ele in key:
            keyStation[ele] = False
        return keyStation

    def toplogical_sort(self):
        queue = []
        station = self.set_keys_station()
        for i in range(self.V):
            for ele in station:
                if not station[ele]:
                    self.toplogical_sort_util(ele, queue, station)
        return queue

    def toplogical_sort_util(self, ele, queue, station):
        station[ele] = True
        for i in station:
            if ele in self.graph[i] and not station[i]:
                station[ele] = False
        if station[ele]:
            queue.append(ele)


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    print(g.toplogical_sort())
