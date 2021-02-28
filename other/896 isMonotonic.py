from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        t = sorted(A)
        if t == A or A[::-1] == t:
            return True
        return False


if __name__ == '__main__':
    A = [1, 3, 2]
    sol = Solution()
    print(sol.isMonotonic(A))
