# http://blog.moertel.com/posts/2013-05-11-recursive-to-iterative.html
# recursive
# TODO
def factorial_rec(n):
    if n == 1:
        return 1
    return n * factorial_rec(n - 1)


# tail recursive
# 尾递归是在函数返回的时候调用本身，并且return 中不能包含表达式, n * factorial(n - 1) 引入了乘法表达式，所以不是一个尾递归
# 我们要删除 n *,只调用函数本身的话，只能扩展这个函数的参数,设置默认参数为1,1 乘以任何数为本身
def factorial1(n, acc=1):
    if n == 1:
        return 1 * acc
    return acc * n * factorial1(n - 1, acc=1)


def factorial2(n, acc=1):
    if n == 1:
        return 1 * acc
    return factorial2(n - 1, acc * n)


# add memory

def factorial_n(n, memo, acc):
    if memo[n] is not None:
        return memo[n]
    if n == 1:
        res = 1
    else:
        res = factorial_n(n - 1, memo, acc * n)
    memo[n] = res
    return res


def factorial_memo(n):
    memo = [None] * (n + 1)
    return factorial_n(n, memo, acc=1)


# the result ------
def factorial(n):
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    for i in range(2, n + 1):
        bottom_up[i] = bottom_up[i - 1] * i
    return bottom_up[n]


if __name__ == '__main__':
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    res = factorial(1000)
    print(res)
