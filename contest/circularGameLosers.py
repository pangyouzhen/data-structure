from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        t = {1}
        j = 1
        m = 1
        while m not in t and j == 1:
            m = m + j * k
            if m > n:
                m = m -n
            t.add(m)
            j += 1
        return list(set([i for i in range(1,n+1)]) - t)
            
if __name__ == "__main__":
    func = Solution().circularGameLosers
    n = 5
    k = 2
    print(func(n,k))