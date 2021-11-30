import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt_num = math.sqrt(c)
        if int(sqrt_num) == sqrt_num:
            return True
        for i in range(1, int(sqrt_num) + 1):
            minus = c - i ** 2
            t = math.sqrt(minus)
            if int(t) == t:
                return True
        return False


if __name__ == '__main__':
    c = 5
    sol = Solution()
    print(sol.judgeSquareSum(c))
