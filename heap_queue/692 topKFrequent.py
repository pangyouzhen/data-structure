from typing import List
from collections import Counter
from queue import PriorityQueue
import pysnooper


class Solution:
    @pysnooper.snoop()
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        c = PriorityQueue()
        for i, v in counter.most_common():
            c.put((-v, i))
        res = []
        while k > 0:
            res.append(c.get()[1])
            k -= 1
        return res


if __name__ == '__main__':
    sol = Solution()
    # words = ["i", "love", "leetcode", "i", "love", "coding"]
    # k = 3
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    print(sol.topKFrequent(words, k))
