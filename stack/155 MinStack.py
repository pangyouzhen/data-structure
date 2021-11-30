class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = []

    def push(self, x: int) -> None:
        self.root.append(x)

    def pop(self) -> None:
        self.root.pop(-1)

    def top(self) -> int:
        return self.root[-1]

    def getMin(self) -> int:
        return min(self.root)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
