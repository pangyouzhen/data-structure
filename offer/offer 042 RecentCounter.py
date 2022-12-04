from bisect import bisect_left, insort
from heapq import heapify


class RecentCounter:
    def __init__(self):
        self.queue = []
        heapify(self.queue)

    def ping(self, t: int) -> int:
        insort(self.queue, t)
        min_ind = bisect_left(self.queue, t - 3000)
        return len(self.queue) - min_ind


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
