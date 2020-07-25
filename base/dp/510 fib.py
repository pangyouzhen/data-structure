from pprint import pprint


def fib_recursive(n):
    if n < 3:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# add memory


def fib_n(n, memo):
    if memo[n] is not None:
        return memo[n]
    elif n == 1 or n == 2:
        res = 1
    else:
        res = fib_n(n - 1, memo) + fib_n(n - 2, memo)
    memo[n] = res
    return res


class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        # 这里为啥是N+1,
        dp = [0] * (N + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        pprint(dp)
        return dp[N]


if __name__ == '__main__':
    sol = Solution()
    print(sol.fib(10))
    print(sol.fib(2))
    print(sol.fib(3))
