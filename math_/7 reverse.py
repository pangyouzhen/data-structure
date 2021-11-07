class Solution:
    def reverse(self, x):
        str_x = str(abs(x))
        val = int("".join(str_x[::-1]))
        if x < 0:
            val = -val
        if (-2 ** 31) <= val <= (2 ** 31):
            return val
        else:
            return 0


if __name__ == '__main__':
    sol = Solution()
    res = sol.reverse(-120)
    print(res)
