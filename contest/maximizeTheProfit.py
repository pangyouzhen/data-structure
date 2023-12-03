from typing import List


class Solution:
    # 这个的时间复杂度是多少
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        offers.sort()
        res = 0
        while offers:
            l = len(offers)
            golds = 0
            tmp = []
            intervals=offers[0]
            if len(offers) == 1:
                golds = offers[-1][-1]
            else:
                for i in range(1, l):
                    overlap_bool,inter,s =  self.overlap(intervals,offers[i])
                    if overlap_bool:
                        tmp.append(inter)
                    else:
                        intervals = inter
                        golds += s
            offers = tmp
            print(offers)
            res = max(golds,res)
        return res
           

    def overlap(self, interval1: List[int], interval2: List[int]):
        if interval2[0] <= interval1[1]:
            # 有重叠区间
            return True,interval2,0
        return False,[interval1[0],interval2[1]],interval1[2]+interval2[2]

if __name__ == "__main__":
    func = Solution().maximizeTheProfit
    # n = 5
    # offers = [[0,0,1],[0,2,2],[1,3,2]]
    n = 5
    offers = [[0,0,1],[0,2,10],[1,3,2]]
    print(func(n,offers))