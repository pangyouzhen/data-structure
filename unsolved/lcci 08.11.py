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
        for i in [25, 15, 10, 5, 1]:
            res = max(1, self.waysToChange_memo(n - i))
        memo[n] = res
        return

    # memo(10) = f(5+5) = f(10) = memo(5) +2


# memo(2) =
# [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 4,]

if __name__ == '__main__':
    n = 10
    sol = Solution()
    # print(sol.waysToChange(10))
    print(sol.waysToChange(2))
