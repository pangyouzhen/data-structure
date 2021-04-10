from typing import List


class Solution:
    def isUgly(self, n):
        res = []

        def ugly_closure(n):
            if n == 1:
                res.append(True)
            for i in (2, 3, 5):
                if (n % i) == 0:
                    ugly_closure(n / i)

        ugly_closure(n)
        print(res)
        return any(res)


if __name__ == '__main__':
    n = 6
    sol = Solution()
    print(sol.isUgly(n))
