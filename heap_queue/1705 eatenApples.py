from typing import List
from heapq import heappop, heappush


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        ans = 0
        pq = []
        i = 0
        while i < len(apples):
            while pq and pq[0][0] <= i:
                heappop(pq)
            if apples[i]:
                heappush(pq, [i+days[i], apples[i]])
            if pq:
                pq[0][-1] -= 1
                if pq[0][1] == 0:
                    heappop(pq)
                ans += 1
            i += 1
        while pq:
            while pq and pq[0][0] <= i:
                heappop(pq)
            if len(pq) == 0:
                break
            p = heappop(pq)
            num = min(p[0] - i, p[1])
            ans += num
            i += num

        return ans


if __name__ == "__main__":
    func = Solution().eatenApples
    apples = [1, 2, 3, 5, 2]
    days = [3, 2, 1, 4, 2]
    print(func(apples, days))
