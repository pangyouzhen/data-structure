from typing import List


class Solution:
    def rotateString(self, A: str, B: str):

        def rotate_one(A):
            return A[1:] + A[0]

        if A == B:
            return True
        n = len(A)
        for i in range(n):
            A = rotate_one(A)
            if A == B:
                return True
        return False


if __name__ == '__main__':
    A = 'abcde'
    B = 'cdeab'
    sol = Solution()
    print(sol.rotateString(A, B))
