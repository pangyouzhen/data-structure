from typing import List
from collections import defaultdict


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        d = defaultdict(int)
        for i,v in enumerate(edges):
            d[v] += i
        init_max = 0
        init_val = 0
        # print(d)
        for i,v in d.items():
            if v > init_val:
                init_max = i
                init_val = v
            elif v == init_val:
                init_max = min(init_max,i)
        return init_max
if __name__ == "__main__":
    func = Solution().edgeScore
    edges = [1,0,0,0,0,7,7,5]
    print(func(edges))