class Solution:
    def reverse(self, x):
        s = str(x)
        s = s[::-1]
        if s[-1] == "-":
            val = -int("".join(s[:-1]))
        else:
            val = int("".join(s))
        if (-2 ** 31 - 1) < val < (2 ** 31 - 1):
            return val
        else:
            return 0


if __name__ == '__main__':
    sol = Solution()
    res = sol.reverse(-120)
    print(res)
