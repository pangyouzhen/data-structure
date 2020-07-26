from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        # 方阵可以这样进行复制，但是非方阵不行 因为结构大小不一样了
        # m = len(A)
        # for i in range(m):
        #     for j in range(i):
        #         A[i][j], A[j][i] = A[j][i], A[i][j]
        # return A
        m, n = len(A), len(A[0])
        ans = [[None] * m for _ in range(n)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                ans[c][r] = val
        return ans


if __name__ == '__main__':
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol = Solution()
    print(sol.transpose(nums))
