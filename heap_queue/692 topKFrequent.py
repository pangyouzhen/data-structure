from typing import List
import heapq
import pysnooper


class Solution:
    @pysnooper.snoop()
    # todo
    # 这里的不一样是在 如果相同的按照首字母的拼写来取
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        pass


if __name__ == '__main__':
    sol = Solution()
    # words = ["i", "love", "leetcode", "i", "love", "coding"]
    # k = 3
    words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    print(sol.topKFrequent(words, k))
