from functools import lru_cache


class Solution:
    @lru_cache()
    def uniquePaths(self, m, n):
        if m <= 0 or n <= 0:
            return 0
        if m == 1 and n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


if __name__ == '__main__':
    sol = Solution()
    assert sol.uniquePaths(3, 2) == 3
    assert sol.uniquePaths(7, 3) == 28
