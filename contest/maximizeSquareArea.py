from typing import List


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.sort()
        vFences.sort()
        hFences.insert(0,1)
        hFences.append(m)
        vFences.insert(0, 1)
        vFences.append(n)
        print(f"{hFences = }")
        print(f"{vFences = }")
        hs = set()
        for i in range(len(hFences)):
            for j in range(i,len(hFences)):
                hs.add(hFences[j]-hFences[i])
        vs = set()
        for i in range(len(vFences)):
            for j in range(i,len(vFences)):
                vs.add(vFences[j]-vFences[i])
        print(f"{hs = }")
        print(f"{vs = }")
        ans = max(hs & vs, default=0)
        MOD = 10**9 + 7
        return ans % MOD if ans**2 else -1
