from typing import List
from collections import Counter


class Solution():
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        len_list = [min(i) for i in rectangles]
        c = Counter(len_list)
        print(c)
        max_key = max(c.keys())
        return c[max_key]

if __name__ =="__main__":
    func = Solution().countGoodRectangles
    nums = [[5,8],[3,9],[5,12],[16,5]]
    print(func(nums))
