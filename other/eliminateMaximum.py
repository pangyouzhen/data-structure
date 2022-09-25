class Solution(object):
    def eliminateMaximum(self, dist, speed):
        val = [i / v for i, v in zip(dist, speed)]
        val.sort()
        a = 0
        for i in range(len(dist)):
            if i >= val[i]:
                a = i
                break
        if a == 0:
            return len(dist)
        else:
            return a


if __name__ == '__main__':
    dist = [1, 1, 2, 3]
    speed = [1, 1, 1, 1]
    sol = Solution()
    print(sol.eliminateMaximum(dist, speed))
