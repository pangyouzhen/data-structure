# # https://blog.csdn.net/qq_38595487/article/details/79686081
# class Solution:
#     def climbStairs_memo(self, n, ls):
#         if ls[n] is not None:
#             return ls[n]
#         elif n == 1:
#             return 1
#         elif n == 2:
#             return 2
#         res = self.climbStairs_memo(n - 1, ls) + self.climbStairs_memo(n - 2, ls)
#         ls[n] = res
#         return ls[n]
#
#     def climbStairs(self, n):
#         ls = [None] * (n + 1)
#         return self.climbStairs_memo(n, ls)
#
#     def no_loop_climbStairs(self, n):
#         if n == 1:
#             return 1
#         elif n == 2:
#             return 2
#         ls = [None] * (n + 1)
#         ls[1] = 1
#         ls[2] = 2
#         for i in range(3, n + 1):
#             ls[i] = ls[i - 1] + ls[i - 2]
#         return ls[n]
#
#
from functools import lru_cache


class Solution2:

    @lru_cache()
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n < 1:
            return 0
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == '__main__':
    sol2 = Solution2()
    assert sol2.climbStairs(2) == 2
    assert sol2.climbStairs(3) == 3
    assert sol2.climbStairs(4) == 5
