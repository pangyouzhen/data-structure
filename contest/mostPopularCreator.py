from typing import List
from collections import defaultdict
from heapq import heappop, heappush


#  自定义比较大小
# class Node:
#     def __init__(self, idv: str, value: int):
#         self.value = value
#         self.idv = idv
#
#     def __lt__(self, other):
#         if self.value > other.value:
#             return self.value
#         elif self.value == other.val:
#             return self.idv < other.idv

#  heap 放一个元组
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        d = defaultdict(list)
        max_val = 0
        max_key = set()
        for c, i, v in zip(creators, ids, views):
            if d.get(c):
                heap = []
                heappush(heap, (-v, i))
                d[c] = [heap, v]
            else:
                heappush(d[c][0], (-v, i))
                d[c][1] += v
            if d[c][1] > max_val:
                max_val = d[c][1]
                max_key = {c}
            elif d[c][1] == max_val:
                max_key.add(c)
        res = []
        for k in max_key:
            v, i = heappop(d[k][0])
            res.append([k, i])
        return res


if __name__ == '__main__':
    func = Solution().mostPopularCreator
    creators = ["alice", "bob", "alice", "chris"]
    ids = ["one", "two", "three", "four"]
    views = [5, 10, 5, 4]
    print(func(creators, ids, views))
