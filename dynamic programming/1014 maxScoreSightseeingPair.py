from typing import List


# class Solution:
#     def maxScoreSightseeingPair(self, A: List[int]) -> int:
#         dp = [0] * len(A)
#         dp[0] = A[0]
#         dp[1] = A[1] + A[0] - 1
#         for i in range(2, len(A)):
#             temp = []
#             for j in range(i):
#                 temp.append(A[i] + A[j] + j - i)
#                 dp[i] = max(temp)
#             # print(temp)
#         # print(dp)
#         return max(dp)


class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 0
        pre_max = A[0] + 0  # 初始值
        for j in range(1, len(A)):
            res = max(res, pre_max + A[j] - j)  # 判断能否刷新res
            pre_max = max(pre_max, A[j] + j)  # 判断能否刷新pre_max， 得到更大的A[i] + i

        return res




if __name__ == '__main__':
    sol = Solution()
    print(sol.maxScoreSightseeingPair([8, 1, 5, 2, 6]))
    print(sol.maxScoreSightseeingPair([5, 3, 1]))
