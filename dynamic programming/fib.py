# recursive


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


def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_n(n, memo)


# bottom up approach

def fib(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[n]


if __name__ == '__main__':
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    res = fib(100000)
    print(res)
