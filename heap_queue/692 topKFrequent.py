from typing import List
import heapq
from collections import Counter


class Word:
    def __init__(self, word, fre) -> None:
        self.word = word
        self.fre = fre

    def __lt__(self, other):
        if self.fre != other.fre:
            return self.fre < other.fre

        return self.word > other.word


class Solution:
    # 这里的不一样是在 如果相同的按照首字母的拼写来取

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heaps = [] 
        for word,fre in counter.items():
            heapq.heappush(heaps,Word(word,fre))
            # 维护一个长度为k的优先队列
            if len(heaps) > k:
                heapq.heappop(heaps)
        heaps.sort(reverse=True)
        return [x.word for x in heaps]


if __name__ == '__main__':
    sol = Solution()
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 3
    # words = ["the", "day", "is", "sunny", "the",
    #  "the", "the", "sunny", "is", "is"]
    # k = 4
    print(sol.topKFrequent(words, k))
