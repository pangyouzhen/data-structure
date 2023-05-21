import math


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        c = 1
        t = 1
        asc = True
        while c <= time:
            if asc and t == n:
                asc = False
                t -= 1
            elif not asc and t == 1:
                asc = True
                t += 1
            elif asc:
                t += 1
            elif not asc:
                t -= 1
            c += 1
        return t


if __name__ == "__main__":
    n = 4
    time = 10
    func = Solution().passThePillow
    print(func(n, time))
