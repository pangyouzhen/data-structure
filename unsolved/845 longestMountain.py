#  动态规划，按顺序递增

#  [1,2,3] 必须是连续的，所以需要记忆上一个山脉尾部的位置
class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [0] * len(A)
        dp[0] = 0
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                pass
