from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        left = 0
        right = 0
        output = []
        while left < len(A) and right < len(B):
            insc = self.intersect(A[left], B[right])
            if insc != None:
                output.append(insc)
            if A[left][1] < B[right][1]:
                left += 1
            else:
                right += 1
        return output

    def intersect(self, ivla, ivlb):
        s = max(ivla[0], ivlb[0])
        e = min(ivla[1], ivlb[1])
        if e >= s:
            return [s, e]
        else:
            return None


if __name__ == '__main__':
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    sol = Solution()
    print(sol.intervalIntersection(A, B))
    A = [[5, 11]]
    B = [[5, 10], [11, 22]]
    print(sol.intervalIntersection(A, B))
