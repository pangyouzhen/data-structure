from typing import List


class Solution():
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        l = len(original)
        if m * n != l:
            return []

        res = []
        for i in range(m):
            res.append(original[i*n:(i+1)*n])
        return res


if __name__ == "__main__":
    func = Solution().construct2DArray
    original = [1, 2, 3]
    m = 1
    n = 3
    print(func(original, m, n))
