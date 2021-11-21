from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l = len(colors)
        dp = [0] * l
        for i in range(l):
            for j in range(i, l):
                if colors[j] != colors[i]:
                    dp[i] = max(j - i, dp[i])
        return max(dp)


if __name__ == '__main__':
    # colors = [1, 1, 1, 6, 1, 1, 1]
    func = Solution().maxDistance
    colors = [1, 8, 3, 8, 3]
    print(func(colors))
