from typing import List


class Solution:
    def isUgly2(self, n):
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

    def isUgly(self, n):
        if n < 1:
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            return self.isUgly(n / 2)
        if n % 3 == 0:
            return self.isUgly(n / 3)
        if n % 5 == 0:
            return self.isUgly(n / 5)
        return False


if __name__ == '__main__':
    n = 6
    sol = Solution()
    print(sol.isUgly(n))
