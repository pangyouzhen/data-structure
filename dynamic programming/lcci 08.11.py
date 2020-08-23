class Solution:
    def waysToChange(self, n: int) -> int:
        global memo
        memo = [None] * (n + 1)
        self.waysToChange_memo(n)
        print(memo)
        return memo[-1]

    def waysToChange_memo(self, n):
        if n < 0:
            return 0
        if memo[n] != None:
            return memo[n]
        for i in [25, 15, 10, 5]:
            res = max(1, self.waysToChange_memo(n - i))
        memo[n] = res
        return res


if __name__ == '__main__':
    n = 10
    sol = Solution()
    print(sol.waysToChange(10))
    print(sol.waysToChange(2))
