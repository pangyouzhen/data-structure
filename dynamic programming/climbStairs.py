# https://blog.csdn.net/qq_38595487/article/details/79686081
#TODO
class Solution:
    def climbStairs_memo(self, n, ls):
        if ls[n] is not None:
            return ls[n]
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        res = self.climbStairs_memo(n - 1, ls) + self.climbStairs_memo(n - 2, ls)
        ls[n] = res
        return ls[n]

    def climbStairs(self, n):
        ls = [None] * (n + 1)
        return self.climbStairs_memo(n, ls)

    def no_loop_climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        ls = [None] * (n + 1)
        ls[1] = 1
        ls[2] = 2
        for i in range(3, n + 1):
            ls[i] = ls[i - 1] + ls[i - 2]
        return ls[n]


if __name__ == '__main__':
    sol = Solution()
    assert sol.climbStairs(2) == 2
    # 1+1, 2
    assert sol.climbStairs(3) == 3
    # 1+1+1, 1+2, 0+1
    assert sol.climbStairs(4) == 5
    # 1+1+1+1, 1+2+1, 1+1+2, 2+1+1, 2+2
    # assert sol.climbStairs(5) == 7

    # 1+1+1+1+1, 1+2+1+1, 1+1+2+1, 2+1+1+1, 1+1+1+2, 2+2+1, 2+1+20
    assert sol.no_loop_climbStairs(2) == 2
    assert sol.no_loop_climbStairs(3) == 3
    assert sol.no_loop_climbStairs(4) == 5
