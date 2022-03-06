from typing import List
from collections import defaultdict

# todo
class Solution:

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        for i in edges:
            dic[i[0]].append(i[1])
        # 并查集还是树进行递归？