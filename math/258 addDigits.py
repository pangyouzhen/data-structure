class Solution:
    def addDigits(self, num: int) -> int:
        t = list(str(num))
        while len(t) > 1:
            t = list(str(sum([int(i) for i in t])))
        return t[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.addDigits(38))
