from typing import List
from collections import defaultdict
import bisect


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        tops = []
        voteCounts = defaultdict(int)
        voteCounts[-1] = -1
        top = -1
        for p in persons:
            voteCounts[p] += 1
            if voteCounts[p] >= voteCounts[top]:
                top = p
            tops.append(top)
        self.tops = tops
        self.times = times

    def q(self, t: int) -> int:
        # 也可以使用内置的二分查找的包来确定 l
        l = bisect.bisect(self.times, t) - 1
        return self.tops[l]


if __name__ == '__main__':
    tv = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    print(tv.q(3))
    print(tv.q(12))
    print(tv.q(25))
    print(tv.q(15))
    print(tv.q(24))
    print(tv.q(8))
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
