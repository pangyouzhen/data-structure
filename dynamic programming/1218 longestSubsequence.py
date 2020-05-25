from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = [0] * n
        for i in range(n):
            for j in range(i):
                # print(f"--------------{i, j}")
                if arr[i] - arr[j] == difference:
                    dp[i] = max(dp[i], dp[j] + 1)
        # print(dp)
        return dp[-1] + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestSubsequence([1, 2, 3, 4], 1))
    print(sol.longestSubsequence([1, 3, 5, 7], 1))
    print(sol.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2))
    print(sol.longestSubsequence([3, 4, -3, -2, -4], -5))
