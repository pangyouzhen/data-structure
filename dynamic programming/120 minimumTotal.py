from typing import List

#  number pyramid : from base to top

a = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

#
# for i in range(3):
#     a[2][i] += min(a[3][i], a[3][i + 1])
#
# print(a[2])
#
# for i in range(2):
#     a[1][i] += min(a[2][i], a[2][i + 1])
# print(a[1])
#
# for i in range(1):
#     a[0][0] += min(a[1][i], a[1][i + 1])
# print(a)


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for j in range(len(triangle) - 1, 0, -1):
            for i in range(j):
                triangle[j - 1][i] += min(triangle[j][i], triangle[j][i + 1])

        return triangle[0][0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTotal(a))
