from typing import List
from collections import Counter


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        r = [i / v for i, v in rectangles]
        c = Counter(r)
        a = 0
        if len(c) == 0:
            return 0
        for i, v in c.items():
            print(v)
            a += (v) * (v - 1) / 2
        return int(a)


if __name__ == '__main__':
    rectangles = [[4, 8], [3, 6], [10, 20], [15, 30]]
    func = Solution().interchangeableRectangles
    print(func(rectangles))
