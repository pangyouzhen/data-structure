import math
import pysnooper


class Solution(object):
    # @pysnooper.snoop()
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        res = 0
        if dist == 1:
            return rungs[-1] - len(rungs)
        for i, v in enumerate(rungs):
            if i == 0:
                minus = v - 0
                if minus > dist:
                    res += math.floor((minus / dist))
                    if (minus / dist) == (minus // dist):
                        res -= 1
            else:
                minus = v - rungs[i - 1]
                if minus > dist:
                    res += math.floor((minus / dist))
                    if (minus / dist) == (minus // dist):
                        res -= 1
        return int(res)


if __name__ == '__main__':
    rungs = [1, 3, 5, 10]
    dist = 2
    # rungs = [3, 4, 6, 7]
    # dist = 1
    # rungs = [12, 24]
    # dist = 4
    sol = Solution()
    print(sol.addRungs(rungs, dist))
