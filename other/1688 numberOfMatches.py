class Solution:
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n != 1:
            match_loop, n = self.get_match(n)
            res += match_loop
        return int(res)

    def get_match(self, n):
        t = n / 2
        if t.is_integer():
            return t, t
        else:
            return (n - 1) / 2, (n - 1) / 2 + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfMatches(14))
