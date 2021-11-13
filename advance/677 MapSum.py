class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, key: str, val: int) -> None:
        self.root[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for word, val in self.root.items():
            if word.startswith(prefix):
                res += val
        return res

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
