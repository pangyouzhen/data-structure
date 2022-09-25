class Solution:
    def countAsterisks(self, s: str) -> int:
        t = 0
        res = 0
        for i in s:
            if i == "|":
                t += 1
            if t % 2 == 0:
                if i == "*":
                    res += 1
        return res


if __name__ == '__main__':
    func = Solution().countAsterisks
    s = "yo|uar|e**|b|e***au|tifu|l"
    print(func(s))
