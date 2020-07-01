class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m = len(A)
        n = len(B)
        dp = [0] * min(m, n)
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i] = max(dp[i - 1], dp[i - 1] + 1)
        print(dp)
        return dp[- 1]


if __name__ == '__main__':
    A = [1, 2, 3, 2, 1]
    B = [3, 2, 1, 4, 7]
    sol = Solution()
    print(sol.findLength(A, B))
