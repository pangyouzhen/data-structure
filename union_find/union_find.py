class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, i) -> int:
        while i != self.parent[i]:
            i = self.parent[i]
        return i

    def is_connect(self, i, j) -> bool:
        return self.find(i) == self.find(j)

    def union(self, i, j) -> None:
        i_root = self.find(i)
        j_root = self.find(j)
        self.parent[i_root] = j_root


if __name__ == "__main__":
    s = 10
    uf =UnionFind(s)
    print(uf.is_connect(2,4))
    uf.union(2,4)
    uf.union(3,5)
    uf.union(8,9)
    print(uf.is_connect(2,9))