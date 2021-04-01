from typing import List


# TODO
class Solution:
    def ll(self, num: int) -> int:

        dp = [0, 1, 2, 6, 7]
        dp.extend([None] * (num - 4))
        if dp[num] is None:
            temp = int(num * (num - 1) / (num - 2)) + (num - 3)
            return temp - self.ll(num - 4)
        else:
            return dp[num]


if __name__ == '__main__':
    a = Solution()
    print(a.ll(10))
