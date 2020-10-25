from typing import List


# 可以分为两部分，第一部分是最长递增子序列，第二部分是最长递减子序列

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A:
            return 0

        n = len(A)
        left = [0] * n
        for i in range(1, n):
            left[i] = (left[i - 1] + 1 if A[i - 1] < A[i] else 0)

        right = [0] * n
        for i in range(n - 2, -1, -1):
            right[i] = (right[i + 1] + 1 if A[i + 1] < A[i] else 0)

        ans = 0
        for i in range(n):
            if left[i] > 0 and right[i] > 0:
                ans = max(ans, left[i] + right[i] + 1)

        return ans


if __name__ == '__main__':
    sol = Solution()
    # nums = [2, 1, 4, 7, 3, 2, 5]
    # print(sol.longestMountain(nums))
    # increase_nums = [2, 1, 4, 7, 5]
    # print(sol.longest_increase_nums(increase_nums))
    nums2 = [2, 0, 2, 0]
    print(sol.longestMountain(nums2))
