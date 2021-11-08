from typing import List
from collections import defaultdict


class Solution:
    #  用原始的dp思想两层for循环是超时的
    def longestSubsequence2(self, arr: List[int], difference: int) -> int:
        dp = [1] * len(arr)
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] - arr[j] == difference:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for v in arr:
            dp[v] = dp[v - difference] + 1
        return max(dp.values())


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestSubsequence([1, 2, 3, 4], 1))
    print(sol.longestSubsequence([1, 3, 5, 7], 1))
    print(sol.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2))
    print(sol.longestSubsequence([3, 4, -3, -2, -4], -5))
