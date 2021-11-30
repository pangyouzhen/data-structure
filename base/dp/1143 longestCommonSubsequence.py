from pprint import pprint


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        ans = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(dp[i][j], ans)
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        pprint(dp)
        return ans


# dp = [
#     [0, 0, 0, 0],
#     [0, 1, 1, 1],
#     [0, 1, 1, 1],
#     [0, 1, 2, 2],
#     [0, 1, 2, 2],
#     [0, 1, 2, 3]
# ]

if __name__ == '__main__':
    text1 = "abcde"
    text2 = "ace"
    sol = Solution()
    print(sol.longestCommonSubsequence(text1, text2))
