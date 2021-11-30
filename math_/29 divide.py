from math import floor, ceil


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = dividend / divisor
        if res > 0:
            res = floor(res)
        elif res < 0:
            res = ceil(res)
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return int(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.divide(0, 1))
