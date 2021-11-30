from functools import lru_cache


class Solution:
    @lru_cache()
    def integerReplacement(self, n: int) -> int:
        # 最小替换 -> 动态规划, 和阶梯题目比较类似，但是从下到上不好定义dp的个数。所以是从上到下的
        # 整个函数意义就是 变为1的所需要的最小次数
        if n == 1:
            return 0
        if n % 2 == 0:
            _ = self.integerReplacement(int(n / 2))
        else:
            _ = min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
        # 所以这里返回的是 1 + 变为1的最小次数，1是每次迭代增加1次
        return 1 + _


if __name__ == '__main__':
    func = Solution().integerReplacement
    n = 1234
    print(func(n))
