from typing import List


#  超时
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = [0] * n
        for i in range(n):
            for j in range(i):
                if arr[i] - arr[j] == difference:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) + 1


class Solution2:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dic = {}
        res = 0

        for i in arr:
            if i - difference in dic:
                dic[i] = dic[i - difference] + 1
            else:
                dic[i] = 1
            res = max(res, dic[i])

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestSubsequence([1, 2, 3, 4], 1))
    print(sol.longestSubsequence([1, 3, 5, 7], 1))
    print(sol.longestSubsequence([1, 5, 7, 8, 5, 3, 4, 2, 1], -2))
    print(sol.longestSubsequence([3, 4, -3, -2, -4], -5))
