from bisect import insort
class SmallestInfiniteSet:

    def __init__(self):
        self.nums = list(range(1,10001))

    def popSmallest(self) -> int:
        return self.nums.pop(0)

    def addBack(self, num: int) -> None:
        if num not in  self.nums:
            insort(self.nums,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)