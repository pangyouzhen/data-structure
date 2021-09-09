from typing import List
import heapq
import pysnooper


class Solution:
    @pysnooper.snoop()
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pass


if __name__ == '__main__':
    sol = Solution()
    # words = ["i", "love", "leetcode", "i", "love", "coding"]
    # k = 3
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    print(sol.topKFrequent(words, k))
